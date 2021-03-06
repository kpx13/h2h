# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
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
from wedding.models import Country, Place, PlaceEventType, PlaceType, PlaceSeason
from gallery.models import Category, Photo
from banner.models import Banner
from review.models import Review
from review.forms import ReviewForm
from blog.models import Article as Blog
from blog.models import Category as BlogCategory
from slideshow.models import Slider
from instagallery.models import Instagallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import config
from livesettings import config_value
from django.conf import settings

PAGINATION_COUNT = 5

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    ban = Banner.objects.all()
    if len(ban) == 0:
        c['banner_link'] = '/'
        c['banner_img'] = ''
    else:
        c['banner_link'] = ban[0].name
        c['banner_img'] = ban[0].image
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    p = Page.get_by_slug(page_name)
    
    if p:
        c.update({'p': p})
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def home(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['slideshow'] = Slider.objects.all()
    c['philosophy'] = Page.get_by_slug('filosofiya-kompanii-na-glavnoj').content
    c['instagallery'] = Instagallery.objects.all().order_by('-media_id')[:5]
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def about(request):
    c = get_common_context(request)
    return render_to_response('about.html', c, context_instance=RequestContext(request))

def get_place(request, place_id):
    return render_to_response('place_on_map.html', {'place': Place.objects.get(id=int(place_id))})

def atlas(request):
    c = get_common_context(request)
    places = Place.objects.all()
    c['country'] = int(request.GET.get('country', 0))
    c['event_type'] = int(request.GET.get('event_type', 0))
    c['place_type'] = int(request.GET.get('place_type', 0))
    c['season'] = int(request.GET.get('season', 0))
    
    if c['country']:
        places = places.filter(country=c['country'])
        if len(places) > 0:
            c['country_coords'] = places[0].coords
    if c['event_type']:
        places = places.filter(event_type=c['event_type'])
    if c['place_type']:
        places = places.filter(place_type=c['place_type'])
    if c['season']:
        places = places.filter(season=c['season'])
    
    c['countries'] = Country.objects.all()
    c['event_types'] = PlaceEventType.objects.all()
    c['place_types'] = PlaceType.objects.all()
    c['seasons'] = PlaceSeason.objects.all()
    c['places'] = places
    return render_to_response('atlas.html', c, context_instance=RequestContext(request))

def philosophy(request):
    c = get_common_context(request)
    p = Page.get_by_slug('philosophy')
    if p:
        c.update({'p': p})
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
    form = OrderForm()
    # filter real countries
    c['countries'] = Country.objects.filter(wt_4=False)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            c['order_ok'] = True
            form = OrderForm()
    c['form'] = form 
    return render_to_response('order.html', c, context_instance=RequestContext(request))

def get_event_type(type):
    try:
        result = PlaceEventType.objects.get(slug=type)
        return(result.id, type, result.name, result.text)
    except:
        return 0

def get_event_type_by_id(type):
    try:
        result = PlaceEventType.objects.get(id=type)
        return(result.id, type, result.name, result.text)
    except:
        return 0

def wedding(request, type):
    items_on_page = 9
    template_name = 'wedding.html'
    sort_column = 'title'
    c = get_common_context(request)
    c['event_type'] = get_event_type(type)
    if not c['event_type']:
        c['event_type'] = get_event_type('official')
    if type == 'official':
        items = Country.objects.filter(wt_1=True)
    if type == 'symbolic':
        items = Country.objects.filter(wt_2=True)
    if type == 'wedding':
        items = Country.objects.filter(wt_3=True)
    if type == 'service':
        items = Country.objects.filter(wt_4=True)
        items_on_page = 18
        template_name = 'services.html'
        sort_column = 'id'

    items = items.order_by(sort_column)
    paginator = Paginator(items, items_on_page)
    page = int(request.GET.get('page', '1'))
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)
    c['page'] = page
    c['page_range'] = paginator.page_range
    if len(c['page_range']) > 1:
        c['need_pagination'] = True
    c['countries'] = items
    return render_to_response(template_name, c, context_instance=RequestContext(request))

def wedding_country(request, type, country):
    c = get_common_context(request)
    c['country'] = Country.get_by_slug(country)
    c['event_type'] = get_event_type(type)
    if not c['event_type']:
        c['event_type'] = get_event_type('official')
    c['places'] = Place.objects.filter(event_type=c['event_type'][0], country=c['country'])
    c['we_create_left'] = Category.objects.get(id=6)
    c['we_create_center'] = Category.objects.get(id=9)
    c['we_create_right'] = Category.objects.get(id=3)
    return render_to_response('wedding_country.html', c, context_instance=RequestContext(request))

def wedding_place(request, type, country, place):
    c = get_common_context(request)
    c['country'] = Country.get_by_slug(country)
    c['place'] = Place.get_by_slug(place)
    c['event_type'] = get_event_type(type)
    if not c['event_type']:
        c['event_type'] = get_event_type_by_id(c['place'].event_type.all()[0].id)
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

def gallery_detail(request, album):
    c = get_common_context(request)
    try:
        album = Category.objects.get(id=album)
        c['album'] = album
    # we have no such gallery
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('gallery_detail.html', c, context_instance=RequestContext(request))


def reviews(request):
    c = get_common_context(request)
    # display all approved reviews with pagination
    items = Review.objects.filter(approved=True)
    paginator = Paginator(items, PAGINATION_COUNT)
    page = int(request.GET.get('page', '1'))
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)
    c['page'] = page
    c['page_range'] = paginator.page_range
    if len(c['page_range']) > 1:
        c['need_pagination'] = True
    c['reviews'] = items
    # get places list to populate place choices
    c['places'] = Place.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            c['review_ok'] = True
    form = ReviewForm()
    c.update({'form': form})
    return render_to_response('reviews.html', c, context_instance=RequestContext(request))

def blog(request, category):
    c = get_common_context(request)
    if not category:
        items = Blog.objects.all()
    else:
        items = Blog.objects.filter(category=category)
        c['curr_cat'] = BlogCategory.objects.get(id=category)
    c['categories'] = BlogCategory.objects.all()
    paginator = Paginator(items, PAGINATION_COUNT)
    page = int(request.GET.get('page', '1'))
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        items = paginator.page(page)
    c['page'] = page
    c['page_range'] = paginator.page_range
    if len(c['page_range']) > 1:
        c['need_pagination'] = True
    c['blog'] = items

    # show vertical banner
    v_banner = Banner.objects.get(id=2)
    c['v_banner_src'] = '/media/' + str(v_banner.image)
    c['v_banner_link'] = v_banner.name
    return render_to_response('blog.html', c, context_instance=RequestContext(request))



