#!/usr/bin/env python
"""view for social_story"""
from django.shortcuts import render
from django.http import HttpResponse


# TODO:Create your views here.
def index(request):
    """view for index"""
    name = "social_story"
    return render(request, 'index.html', {'name': name})
