# -*- coding: utf-8 -*-
from django.db import models

class Banner(models.Model):
    image = models.ImageField(upload_to= 'uploads/slider', max_length=256, verbose_name=u'картинка')
    name  = models.CharField(u'ссылка', max_length=255)
    
    class Meta:
        verbose_name = 'баннер'
        verbose_name_plural = 'баннер'
        
    
    def __unicode__(self):
        return str(self.id)