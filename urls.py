# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from sites import site

admin.autodiscover()


def i18n_javascript(request):
    return admin.site.i18n_javascript(request)


urlpatterns = [
    url(r'$^', RedirectView.as_view(url='admin/')),
    url(r'^admin/', include(site.urls)),
    url(r'^admin/jsi18n', i18n_javascript),  # 如果用到i18n,需要这项映射

    url(r'^admin/(book)/$', site.app_index),
]
