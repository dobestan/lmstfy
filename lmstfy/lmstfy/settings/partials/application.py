import os

import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(BASE_DIR))


SECRET_KEY = 'sbdt^1&-0ynky7nt&vty^*#6sdnaim8gbl&wc&k04@@+v-a00r'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'multisites',
    'search',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'lmstfy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom Context Processors
                'multisites.context_processors.sites',
            ],
        },
    },
]

WSGI_APPLICATION = 'lmstfy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# dj-database-url
# https://github.com/kennethreitz/dj-database-url/

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get(
        'DATABASE_URL',
        'postgres://:@127.0.0.1:5432/lmstfy'
    )),
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Sites Framework
# https://docs.djangoproject.com/en/1.8/ref/contrib/sites/
#
# https://docs.djangoproject.com/en/1.8/ref/contrib/sites/#get-current-site-shortcut
# get_current_site method will now lookup the current site
# based on request.get_host() if the SITE_ID setting is not defined.
#
# SITE_ID = 1
