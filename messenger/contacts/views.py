from django.shortcuts import render
from django.http import JsonResponse

def contacts (request):
    if request.method not in ['GET', 'POST']:
        return JsonResponse({"status" : "Wrong method"})
    return JsonResponse ({"status" : "Заглушка для списка контактов"})

