from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    name = models.CharField('Имя',max_length=64)
    nick = models.CharField('Ник',max_length=64)
    avatar = models.CharField('Аватар',max_length=256, default='')
    last_read_message = models.IntegerField('Последнее прочитанное сообщение id', default=-1)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name']
