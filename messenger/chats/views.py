from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def chats (request):
    return JsonResponse ({"status" : "Заглушка для списка чатов"})

@require_http_methods(['GET', 'POST'])
def chat (request):
    return JsonResponse ({"status" : "Заглушка для страницы чата"})