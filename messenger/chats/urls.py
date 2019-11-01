from django.urls import path
from chats.views import chats, chat_page

urlpatterns = [
    path('', chats, name='chats'),
    path('chat_page/', chat_page, name='chat_page'),
]