Dataset **P. Vivax (Malaria) Infected Human Blood Smears** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/um5gq2ovedk8vrfw2v41n/p.-vivax-malaria-infected-human-blood-smears-DatasetNinja.tar?rlkey=7g2ne1agn22rmjwd1rcmc9k0e&dl=1)

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