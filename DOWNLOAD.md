Dataset **P. Vivax (Malaria) Infected Human Blood Smears** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/0/Y/OJ/JK9SYbPxplXPLTF0RxZRDWLhLbLotUioNmGZm2xbyVflfYOWSf3AYAXQYGp9hd0ItiZiGVlsF9ZCk2m2cNevMtTFBLSSzNcApSmIMWlRefDhIPVtg1ThTMEb0RS3.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='P. Vivax (Malaria) Infected Human Blood Smears', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://data.broadinstitute.org/bbbc/BBBC041/malaria.zip).