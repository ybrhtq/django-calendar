import environ
import json
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()

db_settings = env.str(
    'DB_SETTINGS',
    '{"NAME": "db", "USER": "postgres", "PASSWORD": "postgres", "HOST": "localhost", "PORT": 5432}'
)
try:
    db_settings = json.loads(db_settings)
except json.JSONDecodeError:
    raise ImproperlyConfigured('Error while parsing DB_SETTINGS')
try:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_settings['NAME'],
            'USER': db_settings['USER'],
            'PASSWORD': db_settings['PASSWORD'],
            'HOST': db_settings['HOST'],
            'PORT': db_settings['PORT'],
        }
    }
except KeyError:
    raise ImproperlyConfigured('There are some keys missing in DB_SETTINGS')
