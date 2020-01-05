# thunes_test
* This is the all code in the backend and instruction for this backend
### The backend file struct:
```
.
├── APISecret.ini -> (the ini file to store the api secret, api key and base url)
├── conf
│   └── supervisord.conf -> ( the supervisord config file to start the supervisord)
├── fabfile.py -> (the fab py file to build the python application and upload it pypi server)
├── MAINFEST.in
├── README.md
├── requirements.txt -> (required python package file)
├── setup.cfg
├── setup.py
└── thunes -> (the main folder to store all backend code and test files)
    ├── beneficiary
    │   ├── admin.py -> (the admin file to expose the admin service for this application)
    │   ├── apps.py -> (the apps file to expose the application to settings file)
    │   ├── __init__.py
    │   ├── migrations -> (the sql migration file to mapping with database)
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py -> (the model to define different filed for this application)
    │   ├── serializers.py -> (the file to serialize this application model)
    │   ├── tests.py -> (the file to cover the test cases for this application)
    │   ├── urls.py -> (the file to define the different url mapping with different view function)
    │   └── views.py -> (the file to define the different view function with different post & get method)
    ├── manage.py
    ├── quotation
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── sender
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── thunes
    │   ├── APIAccessGrant.py -> (the common class to integrate with api secret, api key and base url)
    │   ├── db.sqlite3 -> (the sqlite3 database for storing database in the developing phase)
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── base.py -> (the base website setting file)
    │   │   ├── develop.py -> (the extended setting file in developing phase)
    │   │   ├── __init__.py
    │   │   └── product.py -> (the extended setting file in production phase)
    │   ├── urls.py -> (the base url file to expose api docs and define rule with other applications)
    │   └── wsgi.py
    └── transaction
        ├── admin.py
        ├── apps.py
        ├── __init__.py
        ├── migrations
        │   ├── 0001_initial.py
        │   └── __init__.py
        ├── models.py
        ├── serializers.py
        ├── tests.py
        ├── urls.py
        └── views.py
```
* you can know the basic file struct for my website. and this website is wrote using django web framework, and its dataflow is like below (in this example):
```
root folder (thunes) -> thunes/settings.py -> thunes/urls.py -> <app>/urls -> <app>/views -> <app>/model|serializer|admin
```
* there are some commands useful for this website
```
python manage.py runserver -> (to start the web-server but this server is not production usability)
python manage.py test -> (to start all test case wrote in different apps)
```
* the method to migrate this website in your local VM
```
1. make sure the python3.6 and pip installer ready in your VM.
2. pip install virtualenv
3. python3 -m venv venv & source venv/bin/activate
4. pip install --upgrade pip & pip install -r requirements.txt
5. change the APISecret.ini file based on the comment in it
6. cd thunes & python manage.py runserver
```
(PS: better run this web in win, if this pop up some error about sqlite3 version, please pip install django==2.1.8 to downgrade the django framework to be compatiable with sqlite3 version)
* then you can access the api docs /api/docs path to check all exposed apis.
