# -*- coding: utf-8 -*-
__author__ = 'leestrong'

_EMARKET_APPS = set(('book',))


class AuthRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def isAdminApp(self, model):
        if model.__module__.startswith('django.contrib.'):
            return True
        return False

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if self.isAdminApp(model):
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if self.isAdminApp(model):
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if self.isAdminApp(obj1) or self.isAdminApp(obj2):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if 'model' in hints:
            model = hints['model']
            if db == 'auth_db':
                return self.isAdminApp(model)
            elif self.isAdminApp(model):
                return False
        return None


class EmarketRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def use_emarket(self, model):
        if not model.__module__.startswith('django.contrib.'):
            return True
        return False

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if self.use_emarket(model):
            return 'emarket'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if self.use_emarket(model):
            return 'emarket'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.db_tablespace == 'emarket' or \
                        obj2._meta.db_tablespace == 'emarket':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if 'model' in hints:
            model = hints['model']
            if db == 'emarket':
                return self.use_emarket(model)
            elif self.use_emarket(model):
                return False
        return None
