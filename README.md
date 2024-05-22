# Practice_Django NOTES


### Project Setup

- django-admin startproject `project_name`
- cd project_name
- django-admin startapp `app_name`

### Run the app 
- python3 manage.py runserver
- access "http://127.0.0.1:8000/"

### setup url
-  `urls.py` in this file we define URL pattern we will use " the empty string ' ', which matches the root url of the application "
- `views.py` in this file we define the views function that will handles the http request and return http response 

### admin section 

- in admin.py add ``admin.site.register(model class name)``
- do `python3 manage.py makemigrations` . this command tells Django to look for changes in your models and prepare migration files. These files are used to apply the changes to the database schema 
- do `python3 manage.py migrate` This command applies the migration files to your database, creating or altering tables based on your models.
    - use those two commands everytime you made change in databases
- do `python3 manage.py createsuperuser` This command creates a superuser account. Superusers have full access to the Django admin site and can manage all aspects of the database. (use this ONLY ON the first time )