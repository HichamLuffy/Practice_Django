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