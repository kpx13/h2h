# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Country, CountryPhoto, Place, PlacePhoto, PlaceEventType, PlaceSeason, PlaceType

class PlacePhotoInline(admin.TabularInline):
    list_display = ('image', )
    model = PlacePhoto
    extra = 10

class CountryPhotoInline(admin.TabularInline):
    list_display = ('image', )
    model = CountryPhoto
    extra = 10

class PlaceAdmin(admin.ModelAdmin):
    inlines = [ CountryPhotoInline, ]
    list_display = ('name', 'country')

class CountryAdmin(admin.ModelAdmin):
    inlines = [ CountryPhotoInline, ]
    list_display = ('title', 'wt_1', 'wt_2', 'wt_3', 'wt_4')

admin.site.register(Country, CountryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceEventType)
admin.site.register(PlaceType)
admin.site.register(PlaceSeason)