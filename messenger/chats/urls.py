from django.urls import path
from chats.views import chat, create_personal_chat, get_chat_list, add_message, get_message_list, read_messages

urlpatterns = [
    path('chat/<int:chat_id>/', chat, name='chat'),
    path('chat/', chat, name='chat'),
    path('create_personal_chat/', create_personal_chat, name='create_personal_chat'),
    path('get_chat_list/', get_chat_list, name='get_chat_list'),
    path('chat/<int:chat_id>/get_message_list/', get_message_list, name='get_message_list'),
    path('chat/<int:chat_id>/add_message/', add_message, name='add_message'),
    path('chat/<int:chat_id>/read_messages/', read_messages, name='read_message'),
]