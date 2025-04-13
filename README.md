# VitaCareer

### Note
Currently working on this project

### Setting-up virtual environment
```
pip install virtualenv
virtualenv .
.\Scripts\activate
```

Install Django
```
pip install django
```

Create new Django project
```
django-admin startproject vitacareer
```

Run development server
```
python manage.py runserver
```

Setup database
```
python manage.py migrate
```

Create 'home' app
```
python manage.py startapp home
```

To access the admin:
```
python manage.py createsuperuser
``

### Home Page Details

> Navigation Bar
> Login and Register
> Types of users: Admin, Recruiter and Applicant