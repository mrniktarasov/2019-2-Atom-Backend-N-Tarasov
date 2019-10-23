from django.urls import path
from chat_list.views import chat_list

urlpatterns = [
    path('', chat_list, name='char_list'),
]