Dataset **P. Vivax (Malaria) Infected Human Blood Smears** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEyNDFfUC4gVml2YXggKE1hbGFyaWEpIEluZmVjdGVkIEh1bWFuIEJsb29kIFNtZWFycy9wLi12aXZheC0obWFsYXJpYSktaW5mZWN0ZWQtaHVtYW4tYmxvb2Qtc21lYXJzLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogImV0VTVtRE93LzhKRTFFZzMvanM3eDV6Tm5LRG9TRTZKWU1lRVVQMzNIWjQ9In0=)

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