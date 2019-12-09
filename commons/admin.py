# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.admin import UserAdmin, GroupAdmin

import sites

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Permission, admin.ModelAdmin)

sites.site.register(User, UserAdmin)
sites.site.register(Group, GroupAdmin)
sites.site.register(Permission, admin.ModelAdmin)
