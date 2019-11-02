from django.urls import path
from chats.views import chats, chat

urlpatterns = [
    path('', chats, name='chats'),
    path('chat/', chat, name='chat'),
]