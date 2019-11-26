from django.urls import path
from users.views import contacts, user_profile, search_user

urlpatterns = [
    path('', contacts, name='contacts'),
    path('user_profile/', user_profile, name='user_profile'),
    path('search_user/', search_user, name='search_user'),
]