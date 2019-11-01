from django.urls import path
from chats.views import chats

urlpatterns = [
    path('', chats, name='chats'),
]