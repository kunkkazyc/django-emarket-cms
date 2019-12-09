# -*- coding: utf-8 -*-
import time
from django.db import models

from commons.utils import time_utils


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'名称')
    created_time = models.BigIntegerField(verbose_name=u"创建时间", editable=False)

    def get_created_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.created_time / 1000))

    get_created_time.short_description = u"创建时间"

    def save(self, *args, **kwargs):
        self.created_time = time_utils.current_time()
        super(Book, self).save(*args, **kwargs)

    class Meta:
        db_table = 'book'
        verbose_name = u'图书'
        verbose_name_plural = verbose_name
        managed = False
