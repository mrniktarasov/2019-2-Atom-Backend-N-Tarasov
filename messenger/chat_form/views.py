from django.shortcuts import render
from django.http import JsonResponse

def chat_form (request):
    if request.method not in ['GET', 'POST']:
        return JsonResponse({"status" : "Wrong method"})
    return JsonResponse ({"status" : "Заглушка для страницы чата"})