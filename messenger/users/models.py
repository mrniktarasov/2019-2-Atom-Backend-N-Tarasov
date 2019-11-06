from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    name = models.CharField('Name',max_length=64)
    nick = models.CharField('Nick',max_length=64)
    avatar = models.CharField('Avatar',max_length=256, default='')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name']
