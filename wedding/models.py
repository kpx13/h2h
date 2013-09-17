# -*- coding: utf-8 -*-
from django.db import models

class Country(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'название')
    image = models.ImageField(upload_to= 'uploads/wedding/country', max_length=256, verbose_name=u'фото')
    map = models.ImageField(upload_to= 'uploads/wedding/country', max_length=256, verbose_name=u'карта')
    text = models.TextField(verbose_name=u'описание')
    
    class Meta:
        verbose_name = u'страна'
        verbose_name_plural = u'страны'
        
    def __unicode__(self):
        return self.title

class Place(models.Model):
    country = models.ForeignKey(Country, verbose_name=u'страна')
    name = models.TextField(verbose_name=u'название')
    text = models.TextField(verbose_name=u'описание')
    price = models.TextField(verbose_name=u'строчка с ценой')
    service = models.TextField(verbose_name=u'описание доп. услуг')
    image = models.ImageField(upload_to= 'uploads/wedding/place', max_length=256, verbose_name=u'фото')
    file_price = models.FileField(upload_to= 'uploads/wedding/place_docs', max_length=256, verbose_name=u'прайс-лист')
    file_service = models.FileField(upload_to= 'uploads/wedding/place_docs', max_length=256, verbose_name=u'дополнительные услуги')
    file_promo = models.FileField(upload_to= 'uploads/wedding/place_docs', max_length=256, verbose_name=u'рекламный буклет')
    
    class Meta:
        verbose_name = u'место'
        verbose_name_plural = u'места'
    
    def __unicode__(self):
        return self.name
    
    
class PlacePhoto(models.Model):
    place = models.ForeignKey(Place, verbose_name=u'категория')
    image = models.ImageField(upload_to= 'uploads/wedding/place_gallery', max_length=256, verbose_name=u'картинка')
    
    class Meta:
        verbose_name = u'фотография места'
        verbose_name_plural = u'фотографии мест'
    
    def __unicode__(self):
        return self.id