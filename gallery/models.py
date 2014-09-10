# -*- coding: utf-8 -*-
from django.db import models
from wedding.models import Country
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'название')
    year = models.IntegerField(verbose_name=u'год')
    country = models.ForeignKey(Country, verbose_name=u'страна', null=True, blank=True)
    preview_image = models.ImageField(blank=True, null=True, upload_to='uploads/gallery', max_length=256, verbose_name=u'превью')
    text = RichTextField(blank=True, null=True, verbose_name=u'описание галереи')

    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'галерея'
        ordering = ['-year']

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'категория', related_name='photos')
    image = models.ImageField(blank=True, null=True, upload_to='uploads/gallery', max_length=256, verbose_name=u'картинка')
    video = EmbedVideoField(blank=True, null=True, max_length=256, verbose_name=u'видео')
    date = models.DateField(auto_now_add=True, blank=True, verbose_name=u'дата написания')
    sort = models.IntegerField(default=100, verbose_name=u'порядок при сортировке')
    text = RichTextField(blank=True, null=True, verbose_name=u'описание фото')

    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
        ordering = ['sort']

    def __unicode__(self):
        return str(self.id)
