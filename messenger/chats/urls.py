from django.urls import path
from chats.views import chats, chat, create_personal_chat, get_chat_list

urlpatterns = [
    path('', chats, name='chats'),
    path('chat/', chat, name='chat'),
    path('chats/', chat, name='chats'),
    path('create_personal_chat/', create_personal_chat, name='create_personal_chat'),
    path('get_chat_list/', get_chat_list, name='get_chat_list'),
    path('get_chat_list/<int:pk>', get_chat_list, name='get_chat_list'),
]