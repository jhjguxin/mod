#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from django.db import models
import datetime
import mod.settings
import Image

# Create your models here.
# null ：缺省设置为false.通常不将其用于字符型字段上，比如CharField,TextField上.字符型字段如果没有值会返回空字符串。
# blank：该字段是否可以为空。如果为假，则必须有值
"""
四个table 
商品article 门店shop 新闻new 留言message

商品article 编号num 名称name 图片img 备注node hoter 热度hoter

门店shop 名称name 图片img 备注node 热度hoter

新闻new 名称name 发布者writer 时间time 内容content 热度hoter

留言message 主题*sub 内容*content 公司名称*name 公司地址address 邮编zip 联系人*contact 联系电话*call 手机phone 联系传真fax E-mail e-mail
"""
#商品article 编号num 名称name 图片img 备注notes hoter 热度hoter
class Article(models.Model):
  "the class of article"
  num=models.IntegerField(blank=False)
  name=models.CharField(max_length=30,blank=False)
  img=models.ImageField('Image',upload_to='upload-img')
  writer=models.CharField(max_length=30,blank=False)
  wdate=models.DateField(blank=True,null=True,default=datetime.datetime.now())
  notes=models.TextField()
  hoter=models.IntegerField(blank=True,default=0)
#门店shop 名称name 图片img 备注node 热度hoter
class Shop(models.Model):
  "the class of shop"
  name=models.CharField(max_length=30,blank=False)
  img=models.ImageField('Image',upload_to= 'upload-img')
  writer=models.CharField(max_length=30,blank=False)
  wdate=models.DateField(blank=True,null=True,default=datetime.datetime.now())
  notes=models.TextField()
  hoter=models.IntegerField(blank=True,default=0)
#新闻new 名称name 发布者writer 时间time 内容content 热度hoter
class New(models.Model):
  "the class of new"
  name=models.CharField(max_length=30,blank=False)
  writer=models.CharField(max_length=30,blank=False)
  wdate=models.DateField(blank=True,null=True,default=datetime.datetime.now())
  content=models.TextField(blank=False)
  hoter=models.IntegerField(blank=True,default=0)
#留言message 主题*sub 内容*content 公司名称*name 公司地址address 邮编zip 联系人*contact 联系电话*call 手机phone 联系传真fax E-mail e-mail
class Message(models.Model):
  "the class message"
  sub=models.CharField(max_length=30,blank=False)
  content=models.TextField(blank=False)
  name=models.CharField(max_length=30,blank=False)
  address=models.CharField(max_length=30)
  f_zip=models.CharField(max_length=30)
  contact=models.CharField(max_length=30,blank=False)
  call=models.CharField(max_length=30,blank=False)
  phone=models.CharField(max_length=30)
  fax=models.CharField(max_length=30)
  email=models.EmailField(blank=True,verbose_name='e-mail')
