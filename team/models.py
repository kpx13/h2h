# -*- coding: utf-8 -*-
from django.db import models

class Team(models.Model):
    name  = models.CharField(u'имя', max_length=255)
    position  = models.CharField(u'должность', max_length=255)
    image = models.ImageField(upload_to= 'uploads/team', max_length=256, verbose_name=u'фото')
    text  = models.TextField(u'описание', max_length=2000)
    quote  = models.TextField(u'цитита', max_length=500)
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'№ слайдера: 1й, 2й .. 5й')
    
    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'команда'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return self.name