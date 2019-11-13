from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from users.models import User

@require_http_methods(['GET', 'POST'])
def contacts (request):
    return JsonResponse ({"status" : "Заглушка для списка контактов"})

@require_http_methods(['GET', 'POST'])
def user_profile (request):
    return JsonResponse ({"status" : "Заглушка для профиля"})

@require_http_methods(["GET", "POST"])
def search_user (request, user_input=None):
    if user_input is None:
        return JsonResponse({'Error': 'Your input user is None'})
    
    try:
        user_ids = User.objects.filter(id=int(user_input)).values()
    except ValueError:
        user_ids = []

    user_names = User.objects.filter(name=str(user_input)).values()
    user_nicks = User.objects.filter(nick=str(user_input)).values()

    result = [user for user in user_ids]

    for user in user_names:
        if user not in result:
            result.append(user)

    for user in user_nicks:
        if user not in result:
            result.append(user)

    if len(result) == 0:
        return JsonResponse({'response': 'no such users {}'.format(user_input)})

    users = {
        'Users found with {}'.format(user_input) : [
            {
                'user id': res.id,
                'username': res.name,
                'usernick': res.nik,
                'avatar': res.avatar,
            } for res in result
        ]
    }

    return JsonResponse(users)
