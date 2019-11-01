from django.shortcuts import render
from django.http import JsonResponse

def chats (request):
    if request.method not in ['GET', 'POST']:
        return JsonResponse({"status" : "Wrong method"})
    return JsonResponse ({"status" : "Заглушка для списка чатов"})

def chat_page (request):
    if request.method not in ['GET', 'POST']:
        return JsonResponse({"status" : "Wrong method"})
    return JsonResponse ({"status" : "Заглушка для страницы чата"})