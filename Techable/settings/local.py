from .common import *

DEBUG = True

SECRET_KEY = 'test123'


THIRD_PARTY_APPS += [
    'debug_toolbar',
    'django_extensions',
]

INSTALLED_APPS += THIRD_PARTY_APPS

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'techable',
        'USER': 'postgres',
    }
}
