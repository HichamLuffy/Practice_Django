#!/usr/bin/env python
"""view for social_story"""
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages
from django.http import HttpResponse


# TODO:Create your views here.
def main(request):
    """view for main"""
    name = "social_story"
    return render(request, 'main.html', {'name': name})

def signup(request):
    """view for signup"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request, 'Username or Email Taken', extra_tags='error')
                print("Username or Email Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'user created', extra_tags='success')
                # debuging code
                print("user created")
                print(f"username: {username}\nemail: {email}\npassword1: {password1}\npassword2: {password2}")
                # create a profile object  for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                print("profile created")
                print(new_profile)
                return redirect('main')
        else:
            messages.info(request, 'password not matching', extra_tags='error')
            print("password not matching")
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')


def login(request):
    """view for login"""
    return render(request, 'login.html')