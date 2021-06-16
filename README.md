# PyPull
Pull data from an API using Python

# Quickstart

## Create the project directory
$ mkdir [My_Project_Name]

## Create a virtual environment to isolate our package dependencies locally
$ python3 -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`

## Install Django and Django REST framework into the virtual environment
$ pip install django
$ pip install djangorestframework

## Set up a new project with a single application
$ django-admin startproject [Project_Name] .  # Note the trailing '.' character
$ cd tutorial
$ django-admin startapp [App_Name]
$ cd ..

## Set Up your User
$ python manage.py createsuperuser --email admin@example.com --username admin

## Declare your Django Apps
Add your Applicatione and Rest_Framework to the 'INSTALLED_APPS' settings.py file

## Now That The Project Structure Has Been Created Run:
$ python manage.py migrate

### Once Migrating Your Python Module Files Run: 
$ python manage.py runserver

## You can also interact with the API using command line tools such as curl
$ curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@example.com",
        "is_staff": true,
    }
]