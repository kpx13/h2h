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