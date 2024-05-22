#!/usr/bin/env python
"""model for social_story"""
from django.db import models
from django.contrib.auth import get_user_model


# TODO: Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #! need to explain
    id_user = models.IntegerField()
    bio = models.TextField(blank=True, max_length=500)
    profileimg = models.ImageField(upload_to='profile_images', default='profile_images/default0.jpeg')
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True) #! need to explain

    def __str__(self) -> str:
        return self.user.username

#? python3 manage.py makemigrations
#? python3 manage.py migrate
#? python3 manage.py createsuperuser