# -*- coding: utf-8 -*-
from django.db import models
import pytils
from ckeditor.fields import RichTextField

#WEDDING_TYPE = (('1', u'Официальная церемония'),
#                ('2', u'Символическая церемония'),
#                ('3', u'Венчание'))

class Country(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'название')
    image = models.ImageField(upload_to= 'uploads/wedding/country', max_length=256, verbose_name=u'фото')
    map = models.ImageField(upload_to= 'uploads/wedding/country', blank=True, max_length=256, verbose_name=u'карта')
    text = RichTextField(verbose_name=u'описание', blank=True)
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')

    wt_1 = models.BooleanField(blank=True, verbose_name=u'здесь проводятся официальные церемонии')
    wt_2 = models.BooleanField(blank=True, verbose_name=u'здесь проводятся символические церемонии')
    wt_3 = models.BooleanField(blank=True, verbose_name=u'здесь проводятся венчания')
    wt_4 = models.BooleanField(blank=True, verbose_name=u'свадебные услуги')

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
        ordering=['title']

    def __unicode__(self):
        return self.title


class PlaceEventType(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'название')
    text = RichTextField(verbose_name=u'описание события')
    slug = models.CharField(max_length=45, verbose_name=u'URI')

    class Meta:
        verbose_name = u'тип события'
        verbose_name_plural = u'типы событий'

    def __unicode__(self):
        return self.name

class PlaceType(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'название')

    class Meta:
        verbose_name = u'тип места'
        verbose_name_plural = u'типы мест'

    def __unicode__(self):
        return self.name

class PlaceSeason(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'название')

    class Meta:
        verbose_name = u'сезон'
        verbose_name_plural = u'сезоны'

    def __unicode__(self):
        return self.name

class Place(models.Model):
    country = models.ForeignKey(Country, verbose_name=u'страна', related_name='places')
    name = models.CharField(max_length=200, verbose_name=u'название')
    text = RichTextField(verbose_name=u'описание')
    price = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'строчка с ценой')
    service = models.TextField(blank=True, null=True, verbose_name=u'описание доп. услуг')
    image = models.ImageField(upload_to= 'uploads/wedding/place', max_length=256, verbose_name=u'фото')
    file_price = models.FileField(upload_to= 'uploads/wedding/place_docs', blank=True, max_length=256, verbose_name=u'прайс-лист')
    file_service = models.FileField(upload_to= 'uploads/wedding/place_docs', blank=True, max_length=256, verbose_name=u'дополнительные услуги')
    file_promo = models.FileField(upload_to= 'uploads/wedding/place_docs', blank=True, max_length=256, verbose_name=u'рекламный буклет')

    event_type = models.ManyToManyField(PlaceEventType, blank=True, null=True)
    place_type = models.ManyToManyField(PlaceType, blank=True, null=True)
    season = models.ManyToManyField(PlaceSeason, blank=True, null=True)

    coords_x = models.FloatField(verbose_name=u'Широта', blank=True, null=True)
    coords_y = models.FloatField(verbose_name=u'Долгота', blank=True, null=True)

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

    @property
    def coords(self):
        return str(self.coords_x).replace(',', '.') + ', ' +str(self.coords_y).replace(',', '.')

    @property
    def map_content(self):
        return "<b>%s</b><br />%s<br />" % (self.name, self.country.title)

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

class CountryPhoto(models.Model):
    country = models.ForeignKey(Country, verbose_name=u'категория', related_name='photos')
    image = models.ImageField(upload_to='uploads/wedding/place_gallery', max_length=256, verbose_name=u'картинка')

    class Meta:
        verbose_name = u'фотография услуги'
        verbose_name_plural = u'фотографии услуг'

    def __unicode__(self):
        return str(self.id)

