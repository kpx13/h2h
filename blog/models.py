# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'название')
    
    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'
        
    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'заголовок')
    category = models.ForeignKey(Category, verbose_name=u'категория')
    content = RichTextField(verbose_name=u'содержимое')
    image = models.ImageField(upload_to= 'uploads/blog', max_length=256, verbose_name=u'картинка')
    date = models.DateField(auto_now_add=True, blank=True, verbose_name=u'дата написания')
    
    class Meta:
        verbose_name = u'статья'
        verbose_name_plural = u'статьи'
    
    def __unicode__(self):
        return self.title
    
class ArticlePhoto(models.Model):
    article = models.ForeignKey(Article, verbose_name=u'статья', related_name='photos')
    image = models.ImageField(upload_to= 'uploads/blog', max_length=256, verbose_name=u'картинка')
    
    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
    
    def __unicode__(self):
        return str(self.id)