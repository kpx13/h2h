# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Instagallery(models.Model):
    media_id = models.CharField(max_length=48, verbose_name=u'Идентификатор файла')
    link = models.CharField(max_length=256, verbose_name=u'Ссылка на страницу Instagram')
    image_low = models.ImageField(upload_to='uploads/instagallery', verbose_name=u'Фото 306x306')
    image_std = models.ImageField(upload_to='uploads/instagallery', verbose_name=u'Фото 640x640')
    text = RichTextField(blank=True, verbose_name=u'Подпись')
    likes_count = models.IntegerField(default=0, verbose_name=u'Количество лайков')
    processed = models.BooleanField(default=True, verbose_name=u'Обработано')

    class Meta:
        app_label = 'instagallery'
        verbose_name = u'Инстафото'
        verbose_name_plural = u'Инстафото'

    def __unicode__(self):
        return self.link