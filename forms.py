#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#forms.py

from django import forms

class ContactForm(forms.Form):
#  subject=forms.CharField(max_length=100)
#  email=forms.EmailField(required=False,label='You e-mail address')
#  message=forms.CharField(widget=forms.Textarea,min_length=5)
  sub=forms.CharField(max_length=30)
  content=forms.CharField(widget=forms.Textarea,min_length=5)
  name=forms.CharField(max_length=30)
  address=forms.CharField(max_length=30,required=False)
  f_zip=forms.CharField(max_length=30,required=False)
  contact=forms.CharField(max_length=30)
  call=forms.CharField(max_length=30,required=False)
  phone=forms.CharField(max_length=30,required=False)
  fax=forms.CharField(max_length=30,required=False)
  email=forms.EmailField(label='e-mail address:',required=False)
