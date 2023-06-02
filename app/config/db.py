import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


POSTGRESQL = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'db',
            'USER': 'postgres',
            'PASSWORD': '3l3c720n',
            'HOST': '192.168.0.107',
            'PORT': '5432'
        }
}