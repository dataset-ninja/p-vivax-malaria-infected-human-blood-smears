Dataset **P. Vivax (Malaria) Infected Human Blood Smears** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTI0MV9QLiBWaXZheCAoTWFsYXJpYSkgSW5mZWN0ZWQgSHVtYW4gQmxvb2QgU21lYXJzL3AuLXZpdmF4LShtYWxhcmlhKS1pbmZlY3RlZC1odW1hbi1ibG9vZC1zbWVhcnMtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiZUxUTkE3cVNtczhwaktjbWRXMFFhZmZ5cDZ3VitDZzM5eWZlNEhBQnhWVT0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22p.-vivax-%28malaria%29-infected-human-blood-smears-DatasetNinja.tar%22)

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