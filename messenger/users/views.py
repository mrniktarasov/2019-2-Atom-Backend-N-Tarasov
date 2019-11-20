from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from users.models import User

@require_http_methods(['GET', 'POST'])
def contacts (request):
    try:
        users = User.objects.all()
    except User.DoesNotExist:
        return JsonResponse({'Error': 'No users registered'})
    response = {
        'users' : [{
            'username': user.username,
            'id': user.id,
        }] for user in users
    }
    return JsonResponse (response)

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

    if len(user_ids) == 0:
        return JsonResponse({'response': 'no such users {}'.format(user_input)})

    users = {
        'Users found with {}'.format(user_input) : [
            {
                'user id': res.get('id'),
                'username': res.get('username'),
                'usernick': res.get('nick'),
                'avatar': res.get('avatar'),
            } for res in user_ids
        ]
    }

    return JsonResponse(users)

    
