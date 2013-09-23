# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
 

from pages.models import Page
from ideas.models import Article as Idea
from news.models import Article as News
from feedback.forms import FeedbackForm
from order.forms import OrderForm
from order.models import Order
from team.models import Team
from wedding.models import Country, Place, PlacePhoto
from gallery.models import Category, Photo
from review.models import Review
from blog.models import Article as Blog
from blog.models import Category as BlogCategory

import config
from livesettings import config_value
from django.conf import settings


def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    p = Page.get_by_slug(page_name)
    if p.is_service or (page_name == 'cleaning_service'):
        c.update({'services': Page.get_services_links()})
    if p:
        c.update({'p': p})
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def home(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def about(request):
    c = get_common_context(request)
    return render_to_response('about.html', c, context_instance=RequestContext(request))

def philosophy(request):
    c = get_common_context(request)
    return render_to_response('philosophy.html', c, context_instance=RequestContext(request))

def ideas(request):
    c = get_common_context(request)
    c['ideas'] = Idea.objects.all()
    return render_to_response('ideas.html', c, context_instance=RequestContext(request))

def ideas_details(request, page_name):
    c = get_common_context(request)
    c['idea'] = Idea.get_by_slug(page_name)
    return render_to_response('idea.html', c, context_instance=RequestContext(request))

def news(request):
    c = get_common_context(request)
    c['news'] = News.objects.all()
    return render_to_response('news.html', c, context_instance=RequestContext(request))

def news_details(request, page_name):
    c = get_common_context(request)
    c['new'] = News.get_by_slug(page_name)
    return render_to_response('new.html', c, context_instance=RequestContext(request))

def team(request):
    c = get_common_context(request)
    c['team'] = Team.objects.all()
    return render_to_response('team.html', c, context_instance=RequestContext(request))

def contacts(request):
    c = get_common_context(request)
    c.update({'p': Page.get_by_slug('contacts')})
    if request.method == 'GET':
        c.update({'form': FeedbackForm()})
        return render_to_response('contacts.html', c, context_instance=RequestContext(request))
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            c['feedback_ok'] = True
        c.update({'form': form})
        return render_to_response('contacts.html', c, context_instance=RequestContext(request))

def order(request):
    c = get_common_context(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            ord = form.save()
            ord.send_email()
            return render_to_response('order_ok.html', c, context_instance=RequestContext(request))
        else:
            c['form'] = form 
            return render_to_response('order.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()
    
def wedding(request):
    c = get_common_context(request)
    c['countries'] = Country.objects.all()
    return render_to_response('wedding.html', c, context_instance=RequestContext(request))

def wedding_country(request, country):
    c = get_common_context(request)
    c['country'] = Country.get_by_slug(country)
    return render_to_response('wedding_country.html', c, context_instance=RequestContext(request))

def wedding_place(request, country, place):
    c = get_common_context(request)
    c['country'] = Country.get_by_slug(country)
    c['place'] = Place.get_by_slug(place)
    return render_to_response('wedding_place.html', c, context_instance=RequestContext(request))

def gallery(request):
    c = get_common_context(request)
    albums = Category.objects.all()
    years = []
    for a in albums:
        if a.year not in years:
            years.append(a.year)
    c['years'] = years
    countries = []
    for a in albums:
        if a.country not in countries:
            countries.append(a.country)
    c['countries'] = countries
    if request.GET.get('year', ''):
        albums = albums.filter(year=request.GET['year'])
        c['year'] = int(request.GET['year'])
    if request.GET.get('country', ''):
        albums = albums.filter(country=request.GET['country'])
        c['country'] = int(request.GET['country'])
    c['albums'] = albums 
    return render_to_response('gallery.html', c, context_instance=RequestContext(request))

def reviews(request):
    c = get_common_context(request)
    c['reviews'] = Review.objects.all()
    c['places'] = Place.objects.all()
    if request.method == 'POST':
        Review(name=request.POST.get('name', ''), 
               place=Place.objects.get(id=int(request.POST.get('place', '1'))),
               text=request.POST.get('text', '')).save()
        return HttpResponseRedirect('/reviews/')
    return render_to_response('reviews.html', c, context_instance=RequestContext(request))

def blog_category(request, category):
    c = get_common_context(request)
    c['blog'] = Blog.objects.filter(category=category)
    c['categories'] = BlogCategory.objects.all()
    return render_to_response('blog.html', c, context_instance=RequestContext(request))

def blog(request):
    c = get_common_context(request)
    c['blog'] = Blog.objects.all()
    c['categories'] = BlogCategory.objects.all()
    return render_to_response('blog.html', c, context_instance=RequestContext(request))



