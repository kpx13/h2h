# -*- coding: utf-8 -*-
from django.db import models
from wedding.models import Place
from pytils import dt, translit

class Review(models.Model):
    name  = models.CharField(u'имена', max_length=255)
    place  = models.ForeignKey(Place, verbose_name=u'место')
    text = models.TextField(u'текст')
    photo = models.ImageField(upload_to=lambda instance, filename: 'uploads/reviews/' + translit.translify(filename), 
                              null=True, blank=True, max_length=256, verbose_name=u'фото')
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
        ordering = ['-request_date']

    def __unicode__(self):
        return u'%s от %s' % (self.name, dt.ru_strftime(u"%d %B %Y", self.request_date))
