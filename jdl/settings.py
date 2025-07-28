"""
Django settings for jdl project.
"""

import os
import logging
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

def load_docker_secret(name):
    """Load a docker secret, registered as an ENV variable, from the filesystem."""
    location = os.environ.get(name, default=None)
    if not location or not os.path.exists(location):
        logging.warning(f"Could not find docker secret {name} at {location}")
        return None
    
    with open(location, 'r') as f:
        logging.info(f"Loaded docker secret {name}")
        tmp =  f.read().strip()
        if tmp.endswith('\n'):
            tmp = tmp[:-1]
        return tmp

def envget(key, default):
    tmp = os.environ.get(key, default=default)
    if tmp == "":
        return default
    return tmp

def try_docker_else_env(key, default):
    tmp = load_docker_secret(key)
    if tmp:
        return tmp
    return envget(key, default)

SECRET_KEY = envget(
    "DJANGO_SECRET_KEY", default="django-insecure-n*%-(@75nwe&+6fw9y73^fp%()b%p+3^%*dd_ujn=z(!t0id60")

DEBUG = int(envget("DJANGO_DEBUG_MODE", default=1))

_django_allowed_hosts = envget("DJANGO_ALLOWED_HOSTS", default="").split(" ")
ALLOWED_HOSTS = list(set(_django_allowed_hosts + ["localhost", "127.0.0.1", "[::1]"]))

CSRF_TRUSTED_ORIGINS = envget(
    "DJANGO_CSRF_TRUSTED_ORIGINS", default="http://localhost http://127.0.0.1").split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'jdl_web',
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jdl.urls'

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
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'jdl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('fr', _('French')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    'locale',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SHOW_TOOLBAR_CALLBACK = DEBUG
INTERNAL_IPS = [
    "127.0.0.1",
]

# Crispy
CRISPY_ALLOWED_TEMPLATE_PACKS = ["bootstrap4"]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Analytics
PLAUSIBLE_DOMAIN = envget("PLAUSIBLE_DOMAIN", "localhost")
PLAUSIBLE_SCRIPT = envget(
    "PLAUSIBLE_SCRIPT", "http://localhost:8080/js/script.js")