#!/usr/bin/env python
"""social_story URL Configuration"""
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index')
]