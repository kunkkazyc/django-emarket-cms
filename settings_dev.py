# -*- coding: utf-8 -*-

import logging
from common_settings import *

DB_CONF = {
    'HOST': '39.105.158.98',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': '123456',
    'AUTH_DB': 'django_emarket_cms_auth',
    'EMARKET': 'django_emarket_cms',
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_CONF['AUTH_DB'],
        'USER': DB_CONF['USER'],
        'PASSWORD': DB_CONF['PASSWORD'],
        'HOST': DB_CONF['HOST'],
        'PORT': DB_CONF['PORT'],},
    'emarket': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_CONF['EMARKET'],
        'USER': DB_CONF['USER'],
        'PASSWORD': DB_CONF['PASSWORD'],
        'HOST': DB_CONF['HOST'],
        'PORT': DB_CONF['PORT'],},
    'auth_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_CONF['AUTH_DB'],
        'USER': DB_CONF['USER'],
        'PASSWORD': DB_CONF['PASSWORD'],
        'HOST': DB_CONF['HOST'],
        'PORT': DB_CONF['PORT'],},}

OP_CHECK_URL = False

# LOGGING_CONFIG = None
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s',
                    datefmt='%Y:%m:%d-%H:%M:%S', )
daily_rotating_config['filename'] = 'logs/emarket-cms.log'
