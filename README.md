# Baykar Back End Developer Job Application Submission

This project was developed by Ömer Faruk Baran as a submission to fit the requirements by Baykar Technologies.

## Project Setup

For this project to work, python 3.10 or above must be installed in the system. To start the Django project, set up a Python virtual environment first

### For Windows

```bash
python -m venv venv
cd \path\to\venv\Scripts\
.\activate.bat
cd \path\to\where\requirements\file\is
pip install -r requirements.txt
cd \uavrent
python manage.py runserver
```


### For Linux

```shell
python3 -m venv venv
cd /path/to/venv/bin/
source activate
cd /path/to/where/requirements/file/is
pip install -r requirements.txt
cd /uavrent
python manage.py runserver
```

## Front End Demonstration

The front end demonstration is connected to the remotely hosted version of the back end application on my personal AWS VM instance. This has no difference than the localhost version packaged within the repository
If desired the IP address http://3.127.53.229:8000/ has to be replaced with localhost:8000 on the front end client. 

The front end client will not work without a live server. Python already comes with a built in server. To activate it, I have included simple scripts.

### For Windows
```bash
cd \path\to\frontend
.\start.bat
```
### For Linux

```shell
cd /path/to/frontend
chmod +x start.sh
./start.sh
```
if you open localhost:8080 on your browser, the front end will be served and will connect to the remotely hosted back end.

## Back End Administration

if you visit the address the back end is hosted(either local or [remote](http://3.127.53.229:8000/admin/) ) you can access the django built in admin panel to add and change data for debugging and testing the default username is <strong>Baykar</strong>
and the default password is <strong>baykar</strong>

## Back End Models

Fields with * are required/cannot be null.

### User

This is a built in Django Model. Refer to the Django Documentation

### Uav

Id: Integer* <br>
name: Char(100)* <br>
_model: Char(100)* <br>
description: Text <br>
weight: Integer* <br>
category: ForeginKey to UavCategory table <br>
price: Integer* <br>

### UavCategory

Id: Integer* <br>
name: Char(100)* <br>
description: Text <br>


### Rent

Id: Integer* <br>
renter: Foreign Key to User table* <br>
uav: Foregin Key to Uav table* <br>
start_date: DateTime*
end_date: Date

##API Endpoints

All endpoints for this application are accessed with http://hostaddress:8080/api/ . I have followed a simple logic for the end points. Models have their own dedicated end points and the behaviour is determined by
the HTTP request method. 


## Endpoint

http://hostaddress:8080/api/uavcategory/

## POST

### Body

Body has to be application/json. All fields that contain * are required.

### Fields

name: string*
description: string

## GET

### Query Paramemters

format: String(has to be set as json)* <br>
id: Integer <br>

If no Id is provided, it will return all objects <br>

### This syntax applies to all endpoints except User






