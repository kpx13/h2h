# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Country, Place, PlacePhoto

class PhotoInline(admin.TabularInline): 
    list_display = ('image', )
    model = PlacePhoto
    extra = 10
    
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ PhotoInline, ]
    list_display = ('name', 'country')
    
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Country, CountryAdmin)
admin.site.register(Place, PlaceAdmin)