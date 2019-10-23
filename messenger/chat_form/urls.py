from django.urls import path
from chat_form.views import chat_form

urlpatterns = [
    path('', chat_form, name='char_form'),
]