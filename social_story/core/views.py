#!/usr/bin/env python
"""view for social_story"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from .models import Profile
from django.http import JsonResponse, Http404
import requests
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# TODO: n5li landing page like windows kbl mayt7l or like installation d windows mhm dkshi lkdim wslat fikra.

# TODO:Create your views here.

@login_required(login_url='login')
def main(request):
    """view for main"""
    profile = Profile.objects.get(user=request.user)
    return render(request, 'landingpage.html', {'user': request.user, 'profile': profile})

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
                return redirect('login')
        else:
            messages.info(request, 'password not matching', extra_tags='error')
            print("password not matching")
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')


def login(request):
    """view for login"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user)
            return redirect('main')
        else:
            messages.info(request, 'invalid credentials', extra_tags='error')
            print("invalid credentials")
            return redirect('login')
        
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def search_books(request):
    query = request.GET.get('query', '')
    genre = request.GET.get('genre', '')
    books = []

    if query or genre:
        try:
            api_url = f'https://openlibrary.org/search.json?q={query}&subject={genre}'
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                books = data.get('docs', [])
            else:
                return JsonResponse({'error': 'Failed to fetch stories'}, status=response.status_code)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)
    
    return render(request, 'search.html', {'books': books, 'query': query, 'genre': genre})

def book_detail(request, book_key):
    api_url = f'https://openlibrary.org{book_key}.json'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        book = response.json()
        
        # Fetch additional content details
        description = book.get('description')
        if isinstance(description, dict):
            description = description.get('value', '')

        excerpts = book.get('excerpts', [])
        excerpt_texts = [excerpt.get('text', '') for excerpt in excerpts]

        book['description'] = description
        book['excerpts'] = excerpt_texts

        return render(request, 'book_detail.html', {'book': book})
    else:
        raise Http404("Book not found")