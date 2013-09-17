# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'field_1', 'field_2')

admin.site.register(Order, OrderAdmin)