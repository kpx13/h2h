# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

import autocomplete_light
autocomplete_light.autodiscover()
admin.autodiscover()

import settings
import views

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^settings/', include('livesettings.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(r'^$', views.home),
    #url(r'^about/$', views.about),
    url(r'^about/team/$', views.team),
    url(r'^about/philosophy/$', views.philosophy),
    url(r'^about/ideas/(?P<page_name>[\w-]+)/$', views.ideas_details),
    url(r'^about/ideas/$', views.ideas),
    url(r'^news/(?P<page_name>[\w-]+)/$', views.news_details),
    url(r'^news/$', views.news),
    url(r'^contacts/$', views.contacts),
    url(r'^order/$', views.order),
    url(r'^wedding/(?P<type>[\w-]+)/(?P<country>[\w-]+)/(?P<place>[\w-]+)/$', views.wedding_place),
    url(r'^wedding/(?P<type>[\w-]+)/(?P<country>[\w-]+)/$', views.wedding_country),
    url(r'^wedding/(?P<type>[\w-]+)/$', views.wedding),
    url(r'^gallery/(?P<album>[\w-]+)/$', views.gallery_detail),
    url(r'^gallery/$', views.gallery),
    url(r'^reviews/$', views.reviews),
    url(r'^blog/(?P<category>[\w-]+)/$', views.blog),
    url(r'^blog/$', views.blog, {'category': None}),
    url(r'^atlas/$', views.atlas),
    url(r'^(?P<page_name>[\w-]+)/$' , views.page),
    url(r'^get_place/(?P<place_id>[\w-]+)/$', views.get_place),
)
