from pathlib import Path
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-+z-cqsz686h^4!6gn3&+-=6rd#$gjwyhv6boilvrdu^+p2jb&!')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') 
ALLOWED_HOSTS = ['*']

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
    'tailwind',
    'theme',
    'django_browser_reload'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
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

LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'jobs.Enterprise'

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

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ["127.0.0.1",]
ROLEPERMISSIONS_MODULE = "core.roles"