#!/usr/bin/env python
# -*- coding: UTF-8 -*
from django.conf.urls.defaults import *
from mod import views
from mod.modapp.models import Article,New,Shop,Message
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
import os, sys

static = os.path.join(
    os.path.dirname(__file__), 'f_media'
)


urlpatterns = patterns('mod.views',
#    (r'^admin/',include(admin.site.urls)),

     (r'^$', 'index_view'),
     (r"^index.html$",'index_view'),
     (r"^liuyan.html$",'liuyan'),
     (r"^new/(?P<new_id>\d+)/$",'new_detail'),
     (r"^shop/(?P<shop_id>\d+)/$",'shop_detail'),
     (r"^article/(?P<article_id>\d+)/$",'article_detail'),
     (r'^ms_list.html$','ms_list'),
     (r'^mendian.html$','mendian'),
     (r'^fuwu.html$','fuwu'),

#     (r"^ms_list.html$",'ms_list'),
)
#////////


#ms_list={
#    'queryset':Message.objects.order_by('-name'),
#    'template_name':'ms_list.html',
#    'template_object_name':'ms',
#}
#mendian={
#    'queryset':Shop.objects.order_by('name'),
#    'template_name':'mendian.html',
#    'template_object_name':'shop',
#}
#
#fuwu={
#    'queryset':Article.objects.order_by('name'),
#    'template_name':'fuwu.html',
#    'template_object_name':'article',
#}


urlpatterns += patterns('',

#    (r'^ms_list.html$',list_detail.object_list,ms_list),
#    (r'^mendian.html$',list_detail.object_list,mendian),
#    (r'^fuwu.html$',list_detail.object_list,fuwu),
    # Example:
    # (r'^mod/', include('mod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      (r'^admin/', include(admin.site.urls)),
      #(r"^navigation_bar.html$",direct_to_template,{'template':'navigation_bar.html'}),
      (r"^new/\d+/navigation_bar.html$",direct_to_template,{'template':'navigation_bar.html'}),
      (r'^new/\d+/f_media/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/mod/f_media/img'}),#图片链接显示图片
      (r"^shop/\d+/navigation_bar.html$",direct_to_template,{'template':'navigation_bar.html'}),
      (r"^article/\d+/navigation_bar.html$",direct_to_template,{'template':'navigation_bar.html'}),
(r'^article/\d+/f_media/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/mod/f_media/img'}),#图片链接显示图片
#      (r'^shop/\d+/f_media/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/mod/f_media/img'}),#图片链接显示图片
      (r'^article/\d+/f_media/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/mod/f_media/img'}),#图片链接显
      #(r"^main.html$",direct_to_template,{'template':'main.html'}),
#      (r"^templates/index.html$",direct_to_template,{'template':'index.html'}),

      (r"^jianjie.html$",direct_to_template,{'template':'jianjie.html'}),
      (r"^wenhua.html$",direct_to_template,{'template':'wenhua.html'}),
      (r"^guanli.html$",direct_to_template,{'template':'guanli.html'}),
#      (r"^mendian.html$",direct_to_template,{'template':'mendian.html'}),
#      (r"^fuwu.html$",direct_to_template,{'template':'fuwu.html'}),

      (r"^jiameng.html$",direct_to_template,{'template':'jiameng.html'}),
      (r"^lianxi.html$",direct_to_template,{'template':'lianxi.html'}),
#      (r"^right.html$",direct_to_template,{'template':'right.html'}),
      #(r'^f_media/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/mod/f_media/img'}),#图片链接显示图片
      #(r'^f_media/upload-img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/mod/f_media/upload-img'}),
      (r'^upload-img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jhjguxin/Desktop/djcode/mod/f_media/upload-img'})

)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
	    # Images, Css, etc...
	    (r'f_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static }),
	    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/usr/lib/pymodules/python2.6/django/contrib/admin/media' }),
    )
