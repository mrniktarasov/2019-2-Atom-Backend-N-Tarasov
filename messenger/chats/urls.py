from django.urls import path
from chats.views import chats, chat, create_personal_chat, get_chat_list, add_message, get_message_list, read_messages, upload_file, download_file

urlpatterns = [
    path('', chats, name='chats'),
    path('chat/<int:chat_id>', chat, name='chat'),
    path('chat/', chat, name='chats'),
    path('create_personal_chat/', create_personal_chat, name='create_personal_chat'),
    path('get_chat_list/', get_chat_list, name='get_chat_list'),
    path('get_chat_list/<int:user_id>', get_chat_list, name='get_chat_list'),
    path('chat/<int:chat_id>/get_message_list/', get_message_list, name='get_message_list'),
    path('chat/<int:chat_id>/add_message/', add_message, name='add_message'),
    path('chat/<int:chat_id>/read_messages/', read_messages, name='read_message'),
    path('chat/<int:chat_id>/upload_file/', upload_file, name='upload_file'),
    path('chat/<int:chat_id>/download_file/', download_file, name='download_file'),
]