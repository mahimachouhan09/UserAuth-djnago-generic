# UserAuth-djnago-generic
build a user authentication and authorization:

- User signup
- sign in
- logout
- forget password
- update password
- profile update

# Technology-Used
used 
- python,
- django,
- database :-mysql

# Project structure
__UserAuth__ <br>
 |<br>
 +-- templates <br>
 |&nbsp;&nbsp;&nbsp;  |<br>
 |&nbsp;&nbsp;&nbsp;  +--- base.html <br>
 |&nbsp;&nbsp;&nbsp;  +--- index.html <br>
 |&nbsp;&nbsp;&nbsp;  +--- account <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      | <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- change_password.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- login.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- password_reset_complete.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- password_reset_confirm.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- password_reset_done.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- password_reset_email.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- password_reset.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- profile_update.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +--- signup.html <br>
 |    
 +-- UserAuth <br>
 | &nbsp;&nbsp;&nbsp; |  <br>
 | &nbsp;&nbsp;&nbsp; +--- __pycache__ <br>
 | &nbsp;&nbsp;&nbsp; +--- __init__.py <br>
 | &nbsp;&nbsp;&nbsp; +--- settings.py <br>
 | &nbsp;&nbsp;&nbsp; +--- urls.py <br>
 | &nbsp;&nbsp;&nbsp; +--- wsgi.py <br>
 |<br>
 |
 +-- UserLogin <br>
 |&nbsp;&nbsp;&nbsp;  |  <br>
 |&nbsp;&nbsp;&nbsp;  +--- __pycache__ <br>
 |&nbsp;&nbsp;&nbsp;  +--- migrations <br>
 |&nbsp;&nbsp;&nbsp;  +--- __init__.py <br>
 |&nbsp;&nbsp;&nbsp;  +--- admin.py <br>
 |&nbsp;&nbsp;&nbsp;  +--- app.py <br>
 |&nbsp;&nbsp;&nbsp;  +--- forms.py <br>
 |&nbsp;&nbsp;&nbsp;  +--- models.py <br>
 |&nbsp;&nbsp;&nbsp;  +--- tests.py <br>
 |&nbsp;&nbsp;&nbsp;  +--- urls.py <br>
 |&nbsp;&nbsp;&nbsp;  +--- views.py <br>
 |<br>
 |
 +--- db.sqlite3 <br>
 |
 +--- manage.py
 
 # Running Locally

First, clone the repository to your local machine:

```
git clone https://github.com/mahimachouhan09/UserAuth-django

cd UserAuth
```

Install the requirements:

```
pip install -r requirements/dev.txt
```


Create the .env file to the root directory of the project.
You can refer this example file-
 
### [.env.example](./.env.example) 


Apply the database migrations:

```
python manage.py migrate
```

Apply the makemigrations:

```
python manage.py makemigrations
```
Create administrator/super user:
```
python manage.py createsuperuser 


Note: It will prompt to enter username, email and password one by one. Please remember the username and password,
it will be used to login admin area.
```


Finally, run the development server:

```
python manage.py runserver
```

` The site will be available at 127.0.0.1:8000. `
