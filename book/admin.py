#!/usr/bin/env python
# -*- coding: UTF-8 -*-#

from django.contrib import admin
import sites

from book.models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_created_time')

    def __init__(self, *args, **kwargs):
        super(BookAdmin, self).__init__(*args, **kwargs)


admin.site.register(Book, BookAdmin)
sites.site.register(Book, BookAdmin)
