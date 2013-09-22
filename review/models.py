# -*- coding: utf-8 -*-
from django.db import models
from wedding.models import Place
from pytils import dt

class Review(models.Model):
    name  = models.CharField(u'имена', max_length=255)
    place  = models.ForeignKey(Place, verbose_name=u'место')
    text = models.TextField(u'текст')
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
        ordering = ['-request_date']

    def __unicode__(self):
        return u'%s от %s' % (self.name, dt.ru_strftime(u"%d %B %Y", self.request_date))
