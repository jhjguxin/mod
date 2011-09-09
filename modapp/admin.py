#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#admin.py

from django.contrib import admin
from mod.modapp.models import Article,Shop,New,Message

class ArticleAdmin(admin.ModelAdmin):
  list_display=('num','name','img','writer','wdate','notes','hoter')
  list_filter=('hoter',)
  search_fields=('num','name')
  fields=('num','name','img','writer','wdate','notes',)
class ShopAdmin(admin.ModelAdmin):
  list_display=('name','img','writer','wdate','notes','hoter')#不能简单的加入'authors' 一对多类型
  list_filter=('hoter',)
  fields=('name','img','writer','wdate','notes',)
#  ordering=('-publication_date',)
#  fields=('title',)#请注意移除fields选项，以使得编辑页面包含所有字段。）
#  filter_horizontal = ('authors',)针对那些拥有十个以上选项的`` 多对多字段`` 使用filter_horizontal。 这比多选框好用多了
#  filter_vertical=('authors',)
#  raw_id_fields=('publisher',)
class NewAdmin(admin.ModelAdmin):
  list_display=('name','writer','hoter')#不能简单的加入'authors' 一对多类型
  list_filter=('hoter',)
  fields=('name','writer','content')
class MessageAdmin(admin.ModelAdmin):
  list_display=('sub','name','contact','call')#不能简单的加入'authors' 一对多类型

admin.site.register(Article,ArticleAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Message,MessageAdmin)
