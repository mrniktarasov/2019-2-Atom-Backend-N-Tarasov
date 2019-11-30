from django.urls import path, include
from django.contrib.auth import views as auth_views
from auth.views import login, home

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls'), name='social'),
    path('', home, name='home'), 
]