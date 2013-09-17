# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_service', 'title',)
    search_fields = ('title', 'content')

admin.site.register(models.Page, PageAdmin)