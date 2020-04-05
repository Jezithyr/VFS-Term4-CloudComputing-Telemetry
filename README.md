# Telemetry App <!-- omit in toc -->

> a simple telemetry app using a Vue Client, Python Flask Server and Google's Cloud Datastore

### Table of Contents
- [Project Setup](#project-setup)
  - [Basic](#basic)
  - [Authenication](#authenication)
  - [Running Dev Servers](#running-dev-servers)
- [Resources](#resources)
  - [Setting up the Python Client](#setting-up-the-python-client)
  - [Using the Datastore](#using-the-datastore)


## Project Setup

> you need `npm`, `python3` and `Google Cloud SDK Shell` installed for this project
> 
> instructions are for a Windows 10 machine

### Basic

- download the project (either zip or using git url)
- open up root of project in cmd
- run `.\venv\Scripts\activate.bat` to enable python virtual enviroment
- run `pip install -r requirement.txt` to install dependancies


### Authenication

- goto the [google cloud console api credentials screen](https://console.cloud.google.com/apis/credentials) for your project
- create a new set of **service account** credentials
  - make sure one of it's roles is **datastore > cloud datastore owner** to give it permissions to use read / write privalages for cloud datastore
  - you can also make one of its roles **project > owner** for permissions to use all cloud services (not recommended)
- create an access **key** for this service account
- this will download a .json file that will give you access to the account (NOTE: you can only download this once)
- move that json file to the root of the project (same folder as `main.py`) and rename it to `service_account.json`
  - **be extremely careful not to share this with anyone**
    - this means don't commit it to your source control


### Running Dev Servers

- inside the `client` folder run `npm run serve` to start the Vue client
- from the root folder, run `python3 main.py` to start the python server
- access the app at [`localhost:4000`](http://localhost:4000/)

## Resources

### Setting up the Python Client
- [setup a python3 client for google cloud datastore](https://googleapis.dev/python/datastore/latest/index.html)
- [authorizing a server-to-server app *(python server talking to google server)*](https://cloud.google.com/docs/authentication/production#passing_the_path_to_the_service_account_key_in_code)
  - [access control using python](https://cloud.google.com/appengine/docs/standard/python3/access-control)
  - [client auth sample](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/auth/cloud-client/snippets.py)
- [a note on API keys](https://cloud.google.com/docs/authentication/api-keys)
  - basically, google recommends to use service accounts over api keys in most cases

### Using the Datastore
- [python3 API documentation](https://googleapis.dev/python/datastore/latest/client.html)
- [uploading to datastore *(what are entities, properties & keys?)*](https://cloud.google.com/datastore/docs/concepts/entities)