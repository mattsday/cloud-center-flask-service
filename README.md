# CloudCenter Flask Service
This repo includes everything you need to deploy a Flask service in Cisco Cloud Service

## Supported Environments
* Ubuntu (14.04 and 16.04 tested; others should work)
* Debian (8 Jessie tested, others should work)
* CentOS (7 tested, 6 should work)

## Operating
You should zip your flask script and any dependencies up, e.g.
```
zip flaskapp.zip flaskapp.py
```
You can then make this available to the service by setting the following custom parameters:

* ```SCRIPT_LOCATION``` - URL to a zip file containing the script + any other values - the script should be in the root folder of the zip file (e.g. ```./flaskapp.py```)
* ```SCRIPT_NAME``` - the name of the primary python file to execute, for example ```flaskapp.py```
