import os
import shutil
import xml.etree.ElementTree as ET
from collections import defaultdict

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_ds_path: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    file_info = api.file.get_info_by_path(team_id, teamfiles_ds_path)
    file_name_with_ext = file_info.name
    local_path = os.path.join(storage_dir, file_name_with_ext)
    dataset_path = os.path.splitext(local_path)[0]

    if not os.path.exists(dataset_path):
        sly.logger.info(f"Dataset dir '{dataset_path}' does not exist.")
        if not os.path.exists(local_path):
            sly.logger.info(f"Downloading archive '{teamfiles_ds_path}'...")
            api.file.download(team_id, teamfiles_ds_path, local_path)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        path = unpack_if_archive(local_path)
        sly.logger.info(f"Archive '{file_name_with_ext}' was unpacked successfully to: '{path}'.")
        sly.logger.info(f"Dataset dir contains: '{os.listdir(path)}'.")
        sly.fs.silent_remove(local_path)

    else:
        sly.logger.info(
            f"Archive '{file_name_with_ext}' was already unpacked to '{dataset_path}'. Skipping..."
        )
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    teamfiles_dir = "/4import/Malaria Bounding Boxes/archive.zip"
    dataset_path = download_dataset(teamfiles_dir)

    dataset_path = os.path.join(dataset_path, "malaria")

    images_path = os.path.join(dataset_path, "images")
    test_annotations_path = os.path.join(dataset_path, "test.json")
    training_annotations_path = os.path.join(dataset_path, "training.json")

    batch_size = 30
    name_to_class = {}

    image_name_to_data = defaultdict(lambda: defaultdict())

    test_json = sly.json.load_json_file(test_annotations_path)
    training_json = sly.json.load_json_file(training_annotations_path)

    meta = sly.ProjectMeta()

    def collect_annotations(json, split, name_to_class, image_name_to_data, meta=meta):
        for item in json:
            image_name = os.path.basename(item["image"]["pathname"])
            img_height = item["image"]["shape"]["r"]
            img_wight = item["image"]["shape"]["c"]
            # image_path = os.path.join(images_path, image_name)
            objects = item["objects"]
            labels = []
            for obj in objects:
                if "bounding_box" not in obj:
                    sly.logger.warn(f"Object {obj} has no bounding box. Skipping...")
                    continue
                obj_class_name = obj["category"]
                if obj_class_name not in name_to_class:
                    new_obj_class = sly.ObjClass(name=obj_class_name, geometry_type=sly.Rectangle)
                    name_to_class[obj_class_name] = new_obj_class
                    meta = meta.add_obj_class(new_obj_class)

                obj_class = name_to_class[obj_class_name]
                top = obj["bounding_box"]["minimum"]["r"]
                left = obj["bounding_box"]["minimum"]["c"]
                bottom = obj["bounding_box"]["maximum"]["r"]
                right = obj["bounding_box"]["maximum"]["c"]
                rect = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                label = sly.Label(rect, obj_class)
                labels.append(label)

            ann = sly.Annotation(img_size=(img_height, img_wight), labels=labels)
            image_name_to_data[split][image_name] = ann
        return meta

    meta = collect_annotations(test_json, "test", name_to_class, image_name_to_data, meta)
    meta = collect_annotations(training_json, "training", name_to_class, image_name_to_data, meta)

    project = api.project.create(workspace_id, project_name)
    api.project.update_meta(project.id, meta.to_json())

    all_images = os.listdir(images_path)
    diff = (
        set(all_images)
        - set(image_name_to_data["test"].keys())
        - set(image_name_to_data["training"].keys())
    )

    for image_name in diff:
        sly.logger.warn(f"Image {image_name} has no labels, will place it to 'test' split.")
        img = sly.image.read(os.path.join(images_path, image_name))
        img_height, img_wight, _ = img.shape
        image_name_to_data["test"][image_name] = sly.Annotation(img_size=(img_height, img_wight))

    for split, items in image_name_to_data.items():
        pbar = tqdm(desc=f"Processing '{split}' split", total=len(items))
        ds = api.dataset.create(project.id, split)
        for batch in sly.batched(list(items.items()), batch_size=batch_size):
            image_names, anns = zip(*batch)
            image_paths = [os.path.join(images_path, image_name) for image_name in image_names]
            img_infos = api.image.upload_paths(ds.id, image_names, image_paths)
            img_ids = [img_info.id for img_info in img_infos]
            api.annotation.upload_anns(img_ids, anns)
            pbar.update(len(batch))

    sly.logger.info("Deleting temporary app storage files...")
    shutil.rmtree(dataset_path)

    return project
