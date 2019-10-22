from chats.views import chat_list
from django.urls import path

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('category/<int:pk>/', 'chat_category', name='chat_category'),
    path('<chat_id>/', 'chat_detail', name='chat_detail'),
)