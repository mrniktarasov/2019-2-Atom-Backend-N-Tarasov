from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def contacts (request):
    return JsonResponse ({"status" : "Заглушка для списка контактов"})

@require_http_methods(['GET', 'POST'])
def user_profile (request):
    return JsonResponse ({"status" : "Заглушка для профиля"})
