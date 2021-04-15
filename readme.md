=====
TO DO LIST
=====

Todolist is a Django app to create new lists and items for selected list

Quick start
-----------
1. Start project as core .
2. Run the code at terminal which  indicated below  
pip install django-todolist==0.2 
2. Add "'todolist.apps.TodolistConfig'," to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
       
        'todolist.apps.TodolistConfig',
    ]
4. Add static files to settings
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'core/static')
    ]
5. Add templates path to settings
    settings->templates-> DIRs
    DIRS': [os.path.join(BASE_DIR, '..', 'templates')],

6. Include the todolist URLconf in your project urls.py like this:
   Don't forget to import include before!!
    from django.urls import path, include
    path('', include('todolist.urls')),

7. Run pip install psycopg2 at terminal
8. Add db settings to settings file as below
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


9. Run ``python manage.py migrate`` to create the todolist models.

10. Start the development server and visit http://localhost:8000/register/
   