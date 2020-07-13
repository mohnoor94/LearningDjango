# Commands

| Command | Description | Example |
|-------- |------------ |-------- |
| `python -m pip install django` | Install Django | |
| `django-admin startproject [project_name]` | Create a new Django Project | `django-admin startproject django_meeting_planner` |
| `python manage.py runserver` | Run a lightweight web server | |
| `python manage.py startapp [app_name]` | Start a new Django App | `python manage.py startapp meetings` |
| `python manage.py showmigrations` | Show pending migrations from all installed apps | |
| `python manage.py makemigrations` | Auto-create needed migrations for all installed apps | |
| `python manage.py migrate` | Execute all pending migrations from all installed apps | |
| `python manage.py dbshell` | Access a sqlite shell from Django | |
| `python manage.py sqlmigrate [app_name] [migration name or initial number]` | See actual SQL that this migration will run | `python manage.py sqlmigrate meetings 0001` |
| `python manage.py createsuperuser` | Create a super user to be used for administration (and Admin UI) | | 