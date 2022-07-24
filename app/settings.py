import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR,"..", "db.sqlite3"),
    }
}


"""
To connect to an existing postgres database, first:
pip install psycopg2
then overwrite the settings above with:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOURDB',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""

INSTALLED_APPS = ("app.db",)

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Minsk'
USE_I18N = True
USE_TZ = True

# DEBUG setting watchdog.observers
ignore_directories = True
case_sensitive = True
ignore_patterns = [ os.path.join('*', 'app', '*'),
                    os.path.join('*', 'db.sqlite'),
                    os.path.join('*', '__pycache__', '*'),
                    os.path.join('*', 'venv_*', '*'),
                    os.path.join('*', '.gitignore'),
                    os.path.join('*', 'main.py'),
                    os.path.join('*', 'README.*') ]
patterns = [ '*.py' ]
