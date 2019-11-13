from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from chats.models import Chat
from users.models import User
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(['GET', 'POST'])
def chats (request):
    return JsonResponse ({"status" : "Заглушка для списка чатов"})

@require_http_methods(['GET', 'POST'])
def chat (request):
    return JsonResponse ({"status" : "Заглушка для страницы чата"})

@csrf_exempt
@require_http_methods(['POST'])
def create_personal_chat (request):
    chat = Chat.objects.create(topic='Personal chat')
    chat.save()
    return JsonResponse({'Create_personal_chat': 'Personal chat has been created'})

@require_http_methods(['GET','POST'])
def get_chat_list(request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    
    if (pk != 1):
        return JsonResponse({'Error': 'Invalid user'})

    chats = Chat.objects.all()
    if(len(chats) == 0):
        response = {
                'username': 'Nikita',
                'usernick': 'Nik',
                'chats': None,
            }
        return JsonResponse(response)

    response = {
        'username': 'Nikita',
        'usernick': 'Nik',
        'chats':[
            {
                'chat_id': chat.id,
                'is_group_chat': chat.is_group_chat,
                'topic': chat.topic,
                'last_message': chat.last_message,
            }for chat in chats
        ]
    }

    return JsonResponse(response)
