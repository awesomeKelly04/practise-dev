from .base import *

from dj_database_url import parse as db_url
from datetime import timedelta


DEBUG = config('DEBUG', cast=bool)
CORS_ORIGIN_ALLOW_ALL = True


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': config('DATABASE_URL', default='postgres:///practisedevdb', cast=db_url),
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }