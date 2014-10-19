"""
Django settings for BellaStreamWeb project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qv8h)=i44-p50=o(e9eh%zv1=5+70n8#-13n7+zsgmt)9*46bs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'BellaStreamWeb.urls'

WSGI_APPLICATION = 'BellaStreamWeb.wsgi.application'

PHP_CGI = '/usr/local/bin/php-cgi'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, 'templates')

STATIC_URL = '/templates/'

STATICFILES_DIRS = (
	("css", os.path.join(TEMPLATE_ROOT, 'css')),
	("js", os.path.join(TEMPLATE_ROOT, 'js')),
	("images", os.path.join(TEMPLATE_ROOT, 'img')),
	("fonts", os.path.join(TEMPLATE_ROOT, 'fonts')),
)

#template
TEMPLATE_DIRS = (
	TEMPLATE_ROOT,
)
