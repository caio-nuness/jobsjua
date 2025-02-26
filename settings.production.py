from .core.settings import * # Importa as configurações do settings.py base
import os

DEBUG = False #Desativa o debug

ALLOWED_HOSTS = ['seu-dominio.com', 'www.seudominio.com', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'seu_banco_de_dados'),
        'USER': os.environ.get('POSTGRES_USER', 'seu_usuario'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'sua_senha'),
        'HOST': 'db',  # Nome do serviço no docker-compose
        'PORT': '5432',
    }
}

# Configurações adicionais para produção
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')