# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Country, Place, PlacePhoto, PlaceEventType, PlaceSeason, PlaceType

class PhotoInline(admin.TabularInline): 
    list_display = ('image', )
    model = PlacePhoto
    extra = 10
    
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ PhotoInline, ]
    list_display = ('name', 'country')
    
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'wt_1', 'wt_2', 'wt_3')

admin.site.register(Country, CountryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceEventType)
admin.site.register(PlaceType)
admin.site.register(PlaceSeason)