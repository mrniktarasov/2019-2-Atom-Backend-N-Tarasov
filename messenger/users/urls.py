from django.urls import path
from users.views import contacts, user_profile

urlpatterns = [
    path('', contacts, name='contacts'),
    path('user_profile/', user_profile, name='user_profile'),
]