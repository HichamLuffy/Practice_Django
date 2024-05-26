# Practice_Django NOTES

### Project Setup

- Start a new project with `django-admin startproject project_name`
- Navigate into the project directory with `cd project_name`
- Create a new app with `django-admin startapp app_name`

### Run the App

- Start the development server with `python3 manage.py runserver`
- Access the application at "http://127.0.0.1:8000/"

### Setup URL

- In `urls.py`, define URL patterns to map URLs to views. For example, use the empty string `''` to match the root URL of the application.
- In `views.py`, define view functions to handle HTTP requests and return HTTP responses.

### Admin Section

- Register your models in `admin.py` using `admin.site.register(ModelClassName)`
- Apply model changes to the database:
  - Run `python3 manage.py makemigrations` to detect changes in your models and create migration files.
  - Run `python3 manage.py migrate` to apply the migration files to your database, creating or altering tables based on your models.
  - Use these commands whenever you make changes to your models.
- Create a superuser account with `python3 manage.py createsuperuser` to gain full access to the Django admin site. Use this command only the first time you set up your project.


### Setup Login/Sign Up

- Added URL patterns for `signup`, `login`, and `logout` in `urls.py` to map to the respective views.
- Implemented view functions in `views.py`:
  - **Signup View:** Handles user registration. Checks if passwords match and if the username or email already exists. Creates a new user and profile upon successful registration.
  - **Login View:** Authenticates users based on provided credentials. Redirects to the main page upon successful login. Provides feedback for invalid credentials.
  - **Logout View:** Logs out the user and redirects to the login page.
- Important to remember:
  - Use the `login_required` decorator to restrict access to views that require authentication.
  - Always provide feedback to users for actions like registration errors or invalid login attempts.
  - Redirect users appropriately after successful actions (e.g., registration, login, logout).

### Profile Model Notes

- In models.py, defined the Profile model with a foreign key to the User model. This ensures that if a user is deleted, the associated profile will also be deleted.
- Implemented a many-to-many relationship with the User model for favorites, allowing users to have multiple favorites and be favorites of multiple users.

### Display User Info in `main.html`

- To display the username and profile image in `main.html`:
- Modified main.html to display the username and profile image when a user is logged in.
- Ensure the profile image URL is correctly referenced to display the image.
  ```html
  <body>
      <header>
          {% if user %}
          <h1>Welcome {{ user.username }}</h1>
          <img src="{{ profile.profileimg.url }}" alt="{{ user.username }}'s profile picture" style="width:100px;height:100px;">
          <button><a href="{% url 'logout' %}">Logout</a></button>
          {% else %}
          <h1>Welcome to Storytellinaaaaaaaag Platform</h1>
          {% endif %}
          <p>Share and explore stories in various formats!</p>
      </header>
  ```

### General Notes

- Remember to use `python3 manage.py makemigrations` and `python3 manage.py migrate` whenever you make changes to your models.
- When creating forms for signup and login, always handle both GET and POST methods appropriately in the view functions.
- Use Django's `messages` framework to provide feedback to users for actions like registration, login, and logout.
