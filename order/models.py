# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, Template


def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_SEND_TO])


class Order(models.Model):
    field_1  = models.CharField(u'Ваше имя', max_length=255)
    field_2  = models.CharField(u'Дата свадьбы', max_length=255)
    field_3  = models.CharField(u'Тип путешествия', max_length=255)
    field_4  = models.CharField(u'Страна', blank=True, max_length=255)
    field_5  = models.CharField(u'Количество гостей', max_length=255)
    field_6  = models.CharField(u'Контактный телефон', max_length=255)
    field_7  = models.CharField(u'Электронная почта', blank=True, max_length=255)
    field_8 = models.TextField(blank=True, verbose_name=u'Ваши комментарии')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'дата заказа')
    
    class Meta:
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'
        ordering = ['-date']
    
    def __unicode__(self):
        return str(self.date)
    
    def send_email(self):
        subject=u'Поступил новый заказ.',
        body_templ=u"""
{% for field in form %}
{{ field.label }}: {{ field.value }}
{% endfor %}
        """
        body = Template(body_templ).render(Context({'form': self}))
        sendmail(subject, body)    

