#!/usr/bin/env python
"""social_story URL Configuration"""
from django.urls import path
from . import views


urlpatterns = [

    path('', views.main, name='main'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
