# -*- coding: utf-8 -*-

import logging
from common_settings import *

DB_CONF = {
    'HOST': 'xxx的mysql地址',
    'PORT': 'xxx的mysql端口',
    'USER': 'xxx的mysql用户名',
    'PASSWORD': 'xxx的mysql密码',
    'AUTH_DB': 'django_emarket_cms_auth',
    'EMARKET': 'xxx的mysql库',
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
