=====
TO DO LIST
=====

Todolist is a Django app to create new lists and items for selected list

Quick start
-----------

1. Add "'todolist.apps.TodolistConfig'," to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
       
        'todolist.apps.TodolistConfig',
    ]

2. Include the todolist URLconf in your project urls.py like this:
   Don't forget to import include before!!
    from django.urls import path, include
    path('', include('todolist.urls')),

3. Run pip install psycopg2 at terminal
4. Add db settings to settings file as below
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'to-do-list',
            'USER': 'postgres',
            'PASSWORD': 'your-password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


5. Run ``python manage.py migrate`` to create the todolist models.

6. You can start to use after start server