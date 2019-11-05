from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    chat = models.ManyToManyField('chats.Chat')
    name = models.CharField(max_length=64)
    nick = models.CharField(max_length=64)
    avatar = models.CharField(max_length=256, default='')
