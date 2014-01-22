# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class PhotoInline(admin.TabularInline): 
    list_display = ('image', )
    model = models.ArticlePhoto
    extra = 5

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ PhotoInline, ]
    list_display = ('title', 'date')
    search_fields = ('title', 'content')

admin.site.register(models.Category)
admin.site.register(models.Article, ArticleAdmin)