from django.urls import path
from media.views import upload_file, download_file

urlpatterns = [
    path('chat/<int:chat_id>/upload_file/', upload_file, name='upload_file'),
    path('chat/<int:chat_id>/download_file/', download_file, name='download_file'),
]