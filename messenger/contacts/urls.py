from django.urls import path
from contacts.views import contacts

urlpatterns = [
    path('', contacts, name='contacts'),
]