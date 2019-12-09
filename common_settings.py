# -*- coding: utf-8 -*-
import os
import sys
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')

daily_rotating_config = {
    'level': 'INFO',
    'class': 'log_handler.SafeTimedRotatingFileHandler',
    'formatter': 'verbose',
    'filename': 'logs/emarket-cms.log',
    'when': 'MIDNIGHT',
    'backupCount': 30,}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'},
        'simple': {'format': '%(levelname)s %(message)s'},},
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'verbose'},
        'mail_admins': {'level': 'ERROR', 'class': 'django.utils.log.AdminEmailHandler',},
        'daily_rotating': daily_rotating_config,},
    'loggers': {
        '': {'handlers': ['console', 'daily_rotating'],},
        'django': {'handlers': ['console', 'daily_rotating'], 'propagate': False, 'level': 'INFO',},
        'django.request': {'handlers': ['mail_admins', 'daily_rotating'], 'level': 'ERROR', 'propagate': False,}}}

BASE_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5c55^we7jq3y5hf!0w2+tv2+0!8$$x5fig7%ps3veuxm4)2ew^'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# Application definition
INSTALLED_APPS = ['django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions',
                  'django.contrib.messages', 'django.contrib.staticfiles', 'suit', 'django.contrib.admin', 'commons',
                  'book']

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', 'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASE_ROUTERS = ['routers.AuthRouter', 'routers.EmarketRouter']

# TEMPLATE_DIRS = ('templates',)

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Ixmages)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

LOGIN_URL = '/admin/login'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': ['django.template.context_processors.request',
                                   'django.contrib.auth.context_processors.auth',
                                   'django.template.context_processors.i18n',
                                   'django.template.context_processors.csrf',
                                   'django.contrib.messages.context_processors.messages',
                                   ]
        },
    },
]

AES_KEY = "key12345key54321"

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static_files")

EXCEL_TEMPLATE_DIR = os.path.join(BASE_DIR, "templatefile")

BOOK_MODELS = ('book',)

SUIT_CONFIG = {
    'ADMIN_NAME': 'xxx电子商务管理后台',
    'MENU': (
        'sites',
        {'app': 'contenttypes', 'label': u'内容类型', 'models': ('contenttypes',)},
        {'app': 'auth', 'label': u'权限', 'models': ('user', 'group', 'permission')},
        {'app': 'book', 'label': u'图书', 'models': BOOK_MODELS},
    ),
}
