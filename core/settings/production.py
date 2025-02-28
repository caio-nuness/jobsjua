import os
from .base import * # Importa as configurações do settings.py base
from decouple import config

SECRET_KEY = config('DJANGO_SECRET_KEY', 'secret_key')
DEBUG = config('DJANGO_DEBUG', default=False) 

ALLOWED_HOSTS = ['jobsjua.com', 'www.jobsjua.com',]

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

# Configurações adicionais para produção
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')