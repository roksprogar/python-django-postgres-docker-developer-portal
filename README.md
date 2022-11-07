List all (globally) installed python packages

```
pip list
```

Install virtualenv (globally)

```
pip install virtualenv
```

Create a virtual environment called "env"

```
virtualenv env
```

Activate the environment

```
source env/bin/activate
```

Deactivate the environment

```
deactivate
```

Install django (activate the environment or it will be installed globally)

```
pip install django
```

Django admin commands (makemigrations, migrate, runserver, startproject, startapp)

```
django-admin
```

Create a project in the root folder

```
django-admin startproject devsearch .
```

Run the server

```
python manage.py runserver
```
Create an admin user
```
python manage.py createsuperuser
```
