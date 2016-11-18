# CloudCenter Flask Service
This repo includes everything you need to deploy a Flask service in Cisco Cloud Service

## Supported Environments
* Ubuntu (14.04 tested; 16.04 will work when added to CloudCenter)
* CentOS (6 and 7 tested)
* Red Hat (6 and 7 tested)

## Operating
You should zip your flask script and any dependencies up, e.g.
```
zip flaskapp.zip flaskapp.py
```

You can then make this available to the service by setting the following custom parameters:

* ```SCRIPT_LOCATION``` - URL to a zip file containing the script + any other values - the script should be in the root folder of the zip file (e.g. ```./flaskapp.py```)
* ```SCRIPT_NAME``` - the name of the primary python file to execute, for example ```flaskapp.py```

You can also use the following parameters:

* ```SUPER_USER``` - if set to ```Enabled``` then enable password-less sudo
* ```ENABLE_PROXY``` - if set to ```Enabled``` turns on Proxy support
* ```PROXY``` - proxy server in the format ```http://server:port/```
* ```NO_PROXY_HOSTS``` - a list of hosts to never proxy, e.g. ```.cisco.com .intranet```
* ```NO_PROXY_RANGE``` - a list of /24 subnets to not proxy, e.g. 10.0.0 10.0.1

