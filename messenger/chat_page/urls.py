from django.urls import path
from chat_page.views import chat_page

urlpatterns = [
    path('', chat_page, name='char_page'),
]