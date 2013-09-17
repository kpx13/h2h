# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_parameter')
    ordering = ('sort_parameter', )
    
admin.site.register(models.Team, TeamAdmin)