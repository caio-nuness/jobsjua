import os
from .base import * # Importa as configurações do settings.py base
from decouple import config

SECRET_KEY = config('DJANGO_SECRET_KEY', 'secret_key')

DEBUG = config('DJANGO_DEBUG', default=True) 

ALLOWED_HOSTS = ['*',]

if DEBUG == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('POSTGRES_DB', 'database_name'),
            'USER': config('POSTGRES_USER', 'database_user'),
            'PASSWORD': config('POSTGRES_PASSWORD', 'database_password'),
            'HOST': config('POSTGRES_HOST', 'database_host_db'),
            'PORT': config('POSTGRES_PORT', 'database_port_db'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Diretório onde os arquivos estáticos serão coletados
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL para acessar os arquivos estáticos
STATIC_URL = '/static/'

# Diretório onde os arquivos de mídia serão coletados
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

