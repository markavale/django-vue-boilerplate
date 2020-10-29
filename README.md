# django-boilerplate

## Project Details
This Template includes dj-rest-auth for authentication and Token authentication.


## Project setup for virtualenv users
```
python3 -m venv env
pip install -r requirements.txt
python manage.py migrate
```

## Create .env file for your env variables
```
Copy paste this and replace it with your own variables
[settings]
SECRET_KEY = 'sx!6l+&+d(hys6bz)x5lrdfu2$k=6db&tsjz2b&qg-w-nuj#r+'
DJANGO_SETTINGS_MODULE = 'base.settings.dev'

[mysql-database-config] if you're using mysql
NAME=your_db_name
USER=your_db_user
PASSWORD=your_db_password
PORT=your_db_port
HOST=your_db_host

[email]
EMAIL_HOST_PASSWORD = 'your_email_pass'
EMAIL_HOST_USER = 'your_email'
```
See [Configuration Reference of python decouple](https://pypi.org/project/python-decouple/).

## Project setup for pipenv users
```
pipenv shell
pipenv install
python manage.py migrate
```

