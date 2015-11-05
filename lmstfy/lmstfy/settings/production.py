import os

import raven

from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    '*',
]


INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)


# Sentry
# https://getsentry.com/
# https://www.getsentry.com/for/django/

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
}
