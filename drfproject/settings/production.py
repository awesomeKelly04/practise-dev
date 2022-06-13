from email.policy import default
from .base import *
from decouple import config

DEBUG = config('DEBUG', default='False', cast=bool)
CORS_ORIGIN_ALLOW_ALL = True
CONN_MAX_AGE = None

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
    }
}
