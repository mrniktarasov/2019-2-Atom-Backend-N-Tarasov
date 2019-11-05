from django.db import models
from django.apps import apps

class Chat (models.Model):
    is_group_chat = models.BooleanField(null=True, default=False)
    topic = models.CharField(max_length=64, default='Chat')
    last_message = models.TextField(default='')

class Message (models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    content = models.TextField(default='')
    date = models.CharField(max_length=16, default='16:00')
