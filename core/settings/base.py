import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY', 'secret_key')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '192.168.1.7', '192.168.1.1']

INSTALLED_APPS = [
    'jazzmin',
    'rolepermissions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'secret',
    'jobs',
    'django_icons',
    'decouple',
    'tailwind',
    'theme',
    'django_browser_reload'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

if not DEBUG:  # Mais pythonico que DEBUG == False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('POSTGRES_HOST'),
            'PORT': config('POSTGRES_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Diretório onde os arquivos de mídia serão coletados
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'theme/static/css/dist/'),
]

# Diretório para onde os arquivos estáticos serão enviados
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL para acessar os arquivos estáticos
STATIC_URL = '/static/'

# CONFIGURAÇÃO DE MODELS DE USUARIO PERSONALIZADO
AUTH_USER_MODEL = 'jobs.Enterprise'

# CONFIGURAÇÃO DE ICONES
DJANGO_ICONS = {
    "ICONS": {
        "login": {"name": "fa-duotone fa-solid fa-right-to-bracket"},
        "logout": {"name": "fa-solid fa-arrow-right-from-bracket"},
        "delete": {"name": "fa-solid fa-trash"},
        "edit": {"name": "fa-solid fa-pen-to-square"},
        "home": {"name": "fa-solid fa-house"},
        "happy": {"name": "fa-regular fa-face-smile-beam"},
        "arow_right": {"name": "fa-solid fa-right-long"},
        "arow_left": {"name": "fa-solid fa-left-long"},
        "plus": {"name": "fa-solid fa-plus"},
        "eye": {"name": "fa-solid fa-eye"},
    },
}

# CONFIGURAÇÃO DE ROLEPERMISSIONS
ROLEPERMISSIONS_MODULE = "core.roles"

# TAILWINDCSS CONFIGS
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ["127.0.0.1",]
