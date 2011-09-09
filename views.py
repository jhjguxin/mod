#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create your views here.
from django.template import Template,Context,TemplateDoesNotExist
from django.template.loader import get_template as get_Template
#我们不再需要导入 get_template  、 Template 、 Context 和 HttpResponse 。相反，我们导入 django.shortcuts.render_to_response
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from django.views.generic.simple import direct_to_template
import datetime
from django import forms
from mod.forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from mod.modapp.models import Article,New,Shop,Message
from django.views.generic import list_detail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#设置分页数
a=1
b=10
#To retrieve the ''last'' five items in a queryset, you could do this:
#my_queryset.reverse()[:5]
#This example returns the latest Entry in the table, according to the pub_date field:
#Entry.objects.latest('pub_date')
#If your model's Meta specifies get_latest_by, you can leave off the field_name argument to latest(). Django will use the field specified in get_latest_by by default.

import pdb
def index_view(request):
#  mshop=Shop.objects.reverse()[:1]
#  pdb.set_trace()
  mshop=Shop.objects.latest('id')
  marticle=Article.objects.latest('id')
  shop_all=Shop.objects.all().order_by('-wdate')[:4]
  article_all=Article.objects.all().order_by('-wdate')[:4]
  return render_to_response("index.html",{'mshop':mshop,'marticle':marticle,'article_all':article_all,'shop_all':shop_all})



def liuyan(request):
  if request.method=='POST':
    form=ContactForm(request.POST)
    if form.is_valid():
      ct=form.cleaned_data
      ms=Message(sub=ct['sub'],content=ct['content'],name=ct['name'],address=ct['address'],f_zip=ct['f_zip'],contact=ct['contact'],call=ct['call'],phone=ct['phone'],fax=ct['fax'],email=ct['email'],)
      ms.save()
#      ms_list = Message.objects.all()
      return HttpResponseRedirect('ms_list.html')
  else:
    form=ContactForm(initial={'sub': 'I love your site!'})
  return render_to_response('liuyan.html',{'form':form})
#////
def new_detail(request,new_id):
  #Delegate to the generic view and get an HttpResponse.
  contact_list = New.objects.all()
  paginator = Paginator(contact_list, a) # Show 1 contacts per page
  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1
  # If page request (9999) is out of range, deliver last page of results.
  try:
    contacts = paginator.page(page)
  except (EmptyPage, InvalidPage):
    contacts = paginator.page(paginator.num_pages)
  p=New.objects.get(id=page)
  p.hoter=str(int(p.hoter)+1)
  p.save()
  return render_to_response('new_detail.html', {"contacts": contacts})
#bug 导致 列表中的点对点链接失效
def shop_detail(request,shop_id):
  #Delegate to the generic view and get an HttpResponse.
  contact_list = Shop.objects.all()
  paginator = Paginator(contact_list, a) # Show 1 contacts per page
  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1
  # If page request (9999) is out of range, deliver last page of results.
  try:
    contacts = paginator.page(page)
  except (EmptyPage, InvalidPage):
    contacts = paginator.page(paginator.num_pages)
  p=Shop.objects.get(id=page)
  p.hoter=str(int(p.hoter)+1)
  p.save()

  return render_to_response('shop_detail.html', {"contacts": contacts})
#
#  response=list_detail.object_detail(
#    request,
#    queryset=Shop.objects.all(),
#    object_id=shop_id,
#    template_object_name='shop',
#    template_name='shop_detail.html',
#    extra_context={"contacts" : contacts}
#)

  return response

def article_detail(request,article_id):
  #Delegate to the generic view and get an HttpResponse.
  contact_list = Article.objects.all()
  paginator = Paginator(contact_list, a) # Show 1 contacts per page
  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1
  # If page request (9999) is out of range, deliver last page of results.
  try:
    contacts = paginator.page(page)
  except (EmptyPage, InvalidPage):
    contacts = paginator.page(paginator.num_pages)
  p=Article.objects.get(id=page)
  p.hoter=str(int(p.hoter)+1)
  p.save()

  return render_to_response('article_detail.html', {"contacts": contacts})


#////


def ms_list(request):
  #Delegate to the generic view and get an HttpResponse.
  contact_list = Message.objects.all()
  paginator = Paginator(contact_list, b) # Show 1 contacts per page
  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1
  # If page request (9999) is out of range, deliver last page of results.
  try:
    contacts = paginator.page(page)
  except (EmptyPage, InvalidPage):
    contacts = paginator.page(paginator.num_pages)
  return render_to_response('ms_list.html', {"contacts": contacts})


def mendian(request):
  #Delegate to the generic view and get an HttpResponse.
  contact_list = Shop.objects.all()
  paginator = Paginator(contact_list, b) # Show 1 contacts per page
  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1
  # If page request (9999) is out of range, deliver last page of results.
  try:
    contacts = paginator.page(page)
  except (EmptyPage, InvalidPage):
    contacts = paginator.page(paginator.num_pages)
  return render_to_response('mendian.html', {"contacts": contacts})


def fuwu(request):
  #Delegate to the generic view and get an HttpResponse.
  contact_list = Article.objects.all()
  paginator = Paginator(contact_list, b) # Show 1 contacts per page
  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1
  # If page request (9999) is out of range, deliver last page of results.
  try:
    contacts = paginator.page(page)
  except (EmptyPage, InvalidPage):
    contacts = paginator.page(paginator.num_pages)
  return render_to_response('fuwu.html', {"contacts": contacts})


