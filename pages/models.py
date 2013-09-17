# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils
import config

class Page(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'заголовок')
    content = RichTextField(blank=True, verbose_name=u'контент')
    content_right = RichTextField(blank=True, verbose_name=u'контент в блоке справа')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    is_service = models.BooleanField(verbose_name=u'Это услуга?', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Page, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Page.objects.get(slug=page_name)
        except:
            return None
        
    @staticmethod
    def get_services_links():
        return [(p.title, p.slug) for p in  Page.objects.filter(is_service=True)]
    
    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'
        ordering=['title']
        
    def __unicode__(self):
        return self.slug