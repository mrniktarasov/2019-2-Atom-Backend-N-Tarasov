from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from chats.models import Chat
from users.models import User

@require_http_methods(['GET', 'POST'])
def chats (request):
    return JsonResponse ({"status" : "Заглушка для списка чатов"})

@require_http_methods(['GET', 'POST'])
def chat (request):
    return JsonResponse ({"status" : "Заглушка для страницы чата"})

@require_http_methods(['POST'])
def create_personal_chat (request):
    if request.user.id is None:
        return JsonResponse({'Error': 'User id is None'})

    chat = Chat.objects.create(topic='Personal chat')
    chat.user.add(request.POST.user_id)
    chat.save()
    return JsonResponse({'Create_personal_chat': 'Personal chat has been created'})

@require_http_methods(['GET','POST'])
def get_chat_list(request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    
    user_qs = User.objects.all().filter(id=request.POST.user_id)
    if (len(user_qs) == 0):
        return JsonResponse({'Error' : 'User does not exist'})
    user = user_qs.get()
    chats = Chat.objects.filter(user = request.POST.user_id)
    if(len(chats) == 0):
        response = {
            'chats user_id#{}'.format(user.id): {
                'username': user.name,
                'usernick': user.nick,
                'chats': None,
            }
        }
        return JsonResponse(response)

    response = {
        'chats user_id#{}'.format(user.id): {
        'username': user.name,
        'usernick': user.nick,
        'chats': [
            {
                'chat_id': chat.id,
                'is_group_chat': chat.is_group_chat,
                'topic': chat.topic,
                'last_message': chat.last_message,
            }for chat in chats
        ]
        }
    }

    return JsonResponse(response)
