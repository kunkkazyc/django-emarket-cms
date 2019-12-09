# -*- coding: utf-8 -*-
__author__ = 'leestrong'

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
