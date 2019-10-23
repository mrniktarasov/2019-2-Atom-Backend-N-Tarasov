from django.urls import path
from profile_list.views import profile_list

urlpatterns = [
    path('', profile_list, name='profile_list'),
]