from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class User (AbstractBaseUser):
    chat = models.ManyToManyField('chats.Chat')
    name = models.CharField(max_length=64)
    nick = models.CharField(max_length=64)
    avatar = models.CharField(max_length=256, default='')
