from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Malaria Bounding Boxes"
PROJECT_NAME_FULL: str = "P. Vivax (Mlaria) Infected Human Blood Smears"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_3_0_IGO()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Biomedical()]
CATEGORY: Category = Category.Biology(extra=Category.Medical())

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2019-03-11"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://bbbc.broadinstitute.org/BBBC041/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1431039
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/malaria-bounding-boxes"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################

DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://data.broadinstitute.org/bbbc/BBBC041/malaria.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "red blood cell":[230, 25, 75], "trophozoite":[60, 180, 75], "difficult":[255, 225, 25], "ring":[0, 130, 200], "schizont":[245, 130, 48], "gametocyte":[145, 30, 180],  "leukocyte":[70, 240, 240]
}

# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://arxiv.org/abs/1804.09548"
CITATION_URL: Optional[str] = "https://bbbc.broadinstitute.org/BBBC041/"
AUTHORS: Optional[List[str]] = [
    "Jane Hung",
    "Deepali Ravel",
    "Stefanie C.P. Lopes",
    "Gabriel Rangel",
    "Odailton Amaral Nery",
    "Benoit Malleret",
    "Francois Nosten",
    "Marcus V. G. Lacerda",
    "Marcelo U. Ferreira",
    "Laurent Rénia",
    "Manoj T. Duraisingh",
    "Fabio T. M. Costa",
    "Matthias Marti",
    "Anne E. Carpenter",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Broad Institute, UK"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.broadinstitute.org/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,        
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
