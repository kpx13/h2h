# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'request_date', 'approved')
    ordering = ('request_date', )

admin.site.register(Review, ReviewAdmin)