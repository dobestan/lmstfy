from .partials import *


INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)


# django-extensions
# http://django-extensions.readthedocs.org

# Always use IPython for shell_plus
SHELL_PLUS = "ipython"
