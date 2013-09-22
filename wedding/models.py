# -*- coding: utf-8 -*-
from django.db import models
import pytils
from ckeditor.fields import RichTextField

class Country(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'название')
    image = models.ImageField(upload_to= 'uploads/wedding/country', max_length=256, verbose_name=u'фото')
    map = models.ImageField(upload_to= 'uploads/wedding/country', blank=True, max_length=256, verbose_name=u'карта')
    text = RichTextField(verbose_name=u'описание', blank=True)
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Country, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Country.objects.get(slug=page_name)
        except:
            return None
    
    class Meta:
        verbose_name = u'страна'
        verbose_name_plural = u'страны'
        ordering=['id']
        
    def __unicode__(self):
        return self.title

class Place(models.Model):
    country = models.ForeignKey(Country, verbose_name=u'страна', related_name='places')
    name = models.CharField(max_length=200, verbose_name=u'название')
    text = RichTextField(verbose_name=u'описание')
    price = models.CharField(max_length=200, verbose_name=u'строчка с ценой')
    service = models.TextField(verbose_name=u'описание доп. услуг')
    image = models.ImageField(upload_to= 'uploads/wedding/place', max_length=256, verbose_name=u'фото')
    file_price = models.FileField(upload_to= 'uploads/wedding/place_docs', blank=True, max_length=256, verbose_name=u'прайс-лист')
    file_service = models.FileField(upload_to= 'uploads/wedding/place_docs', blank=True, max_length=256, verbose_name=u'дополнительные услуги')
    file_promo = models.FileField(upload_to= 'uploads/wedding/place_docs', blank=True, max_length=256, verbose_name=u'рекламный буклет')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.name)
        super(Place, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Place.objects.get(slug=page_name)
        except:
            return None
    
    class Meta:
        verbose_name = u'место'
        verbose_name_plural = u'места'
    
    def __unicode__(self):
        return self.name
    
    
class PlacePhoto(models.Model):
    place = models.ForeignKey(Place, verbose_name=u'категория', related_name='photos')
    image = models.ImageField(upload_to= 'uploads/wedding/place_gallery', max_length=256, verbose_name=u'картинка')
    
    class Meta:
        verbose_name = u'фотография места'
        verbose_name_plural = u'фотографии мест'
    
    def __unicode__(self):
        return str(self.id)