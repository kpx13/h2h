# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
import datetime
from django.conf import settings
from django.core.mail import send_mail


class OrderServices(models.Model):
    name  = models.CharField(u'название', max_length=255)
    
    class Meta:
        verbose_name = u'услуга'
        verbose_name_plural = u'дополнительные услуги'
    
    def __unicode__(self):
        return self.name

class Order(models.Model):
    field_1  = models.CharField(u'Ваше имя', max_length=255)
    field_2  = models.CharField(u'Дата свадьбы', max_length=255)
    field_3  = models.CharField(u'Тип путешествия', blank=True, max_length=255)
    field_4  = models.CharField(u'Страна', blank=True, max_length=255)
    field_5  = models.CharField(u'Количество гостей', max_length=255)
    field_6  = models.CharField(u'Контактный телефон', max_length=255)
    field_7  = models.CharField(u'Электронная почта', blank=True, max_length=255)
    field_8 = models.TextField(blank=True, verbose_name=u'Ваши комментарии')
    services = models.ManyToManyField(OrderServices, blank=True, verbose_name=u'Дополнительные услуги')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'дата заказа')
    
    class Meta:
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'
        ordering = ['-date']
    
    def __unicode__(self):
        return str(self.date)

