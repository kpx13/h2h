# -*- coding: utf-8 -*-
from django.db import models
from wedding.models import Country

class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'название')
    year = models.IntegerField(verbose_name=u'год')
    country = models.ForeignKey(Country, verbose_name=u'страна')
    
    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'галлерея'
    
    def __unicode__(self):
        return self.title

class Photo(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'категория')
    image = models.ImageField(upload_to= 'uploads/gallery', max_length=256, verbose_name=u'картинка')
    date = models.DateField(auto_now_add=True, blank=True, verbose_name=u'дата написания')
    
    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
    
    def __unicode__(self):
        return self.id