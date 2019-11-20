from django.urls import path
from chats.views import chats, chat, create_personal_chat, get_chat_list, add_message, get_message_list, readed_messages

urlpatterns = [
    path('', chats, name='chats'),
    path('chat/<int:pk>', chat, name='chat'),
    path('chat/', chat, name='chats'),
    path('create_personal_chat/', create_personal_chat, name='create_personal_chat'),
    path('get_chat_list/', get_chat_list, name='get_chat_list'),
    path('get_chat_list/<int:pk>', get_chat_list, name='get_chat_list'),
    path('chat/<int:pk>/get_message_list/', get_message_list, name='get_message_list'),
    path('chat/get_message_list/<int:pk>', get_message_list, name='get_message_list'),
    path('chat/<int:pk>/add_message/', add_message, name='add_message'),
    path('chat/<int:pk>/readed_messages/', readed_messages, name='readed_message'),
]