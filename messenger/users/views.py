from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from users.models import User
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(['GET', 'POST'])
def contacts (request):
    try:
        users = User.objects.all()
    except User.DoesNotExist:
        return JsonResponse({'Error': 'No users registered'}, status=404)
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

@csrf_exempt
@require_http_methods(["GET"])
def search_user (request):
    username = request.GET.get('username')
    if username is None:
        return JsonResponse({'Error': 'Your input user is None'}, status=400)
    
    user_name = User.objects.filter(username__contains = username).values()
    print(user_name)

    if not user_name:
        return JsonResponse({'response': 'no such users {}'.format(username)}, status=404)

    users = {
        'Users found with {}'.format(username) : [
            {
                'user id': res.get('id'),
                'username': res.get('username'),
                'usernick': res.get('nick'),
                'avatar': res.get('avatar'),
            } for res in user_name
        ]
    }

    return JsonResponse(users)
