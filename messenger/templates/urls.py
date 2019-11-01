from django.urls import path
from templates.views import main_page

urlpatterns = [
    path('', main_page, name='main_page'),
]