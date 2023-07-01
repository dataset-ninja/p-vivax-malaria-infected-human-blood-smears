Dataset **Malaria Bounding Boxes** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/r/i/rN/6AvMzDBY8eY3u2ckaSavF5uPszoCiqnePuP1FP8AWNMKoFm25wSjm12i35hhoRyC429Ea4b3hqApWXzPTGTe0UGgaAfphdoqzqbbFmeGYl6yQ5v6cLcq9EZTrSR6.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Malaria Bounding Boxes', dst_path='~/dtools/datasets/Malaria Bounding Boxes.tar')
```
The data in original format can be 🔗[downloaded here](https://data.broadinstitute.org/bbbc/BBBC041/malaria.zip)