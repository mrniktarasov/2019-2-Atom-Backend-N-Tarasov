from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Message
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from .forms import MessageForm, CreatePersonalChat
import datetime

@require_http_methods(['GET', 'POST'])
def chats (request):
    return JsonResponse ({"status" : "Заглушка для списка чатов"})

@require_http_methods(['GET', 'POST'])
def chat (request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    try:
        current_chat = Chat.objects.filter(id=pk)[0]
    except Chat.DoesNotExist:
        return JsonResponse({'Error': 'Chat#{} does not exist'.format(pk)})
    return JsonResponse({
        'is group chat': current_chat.is_group_chat,
        'topic': current_chat.topic,
        'last message': current_chat.last_message,
    })
    

@csrf_exempt
@require_http_methods(['POST'])
def create_personal_chat (request):
    form = CreatePersonalChat(request.POST)
    if form.is_valid(): 
        chat = form.save()
        chat.topic = 'Personal chat'
        chat.user.add(1)
        chat.save()
        return JsonResponse({'Create_personal_chat': 'Personal chat has been created'})
    return JsonResponse({'Errors' : form.errors}, status=400)

@require_http_methods(['GET','POST'])
def get_chat_list(request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    try:
        user = User.objects.filter(id=pk)[0]
    except User.DoesNotExist:
        user = None
    if  user == None:
        return JsonResponse({'response': 'no such users {}'.format(pk)})
    chats = Chat.objects.filter(user=pk).values()
    if(len(chats) == 0):
        return JsonResponse({'Error': 'User has no chats'})

    response = {
        'name': user.name,
        'username': user.username,
        'usernick': user.nick,
        'chats':[
            {
                'chat_id': chat.get('id'),
                'is_group_chat': chat.get('is_group_chat'),
                'topic': chat.get('topic'),
                'last_message': chat.get('last_message'),
            }for chat in chats
        ]
    }

    return JsonResponse(response)

@csrf_exempt
@require_http_methods(['POST'])
def add_message(request, pk=None):
    if pk == None:
        return JsonResponse({'Error': 'invalid chat {}'.format(pk)})
    current_chat = Chat.objects.filter(id=pk)[0]
    user_id = request.POST['user_id']
    if not current_chat:
        return JsonResponse({'Error':'Chat#{} not found'.format(pk)})
 
    form = MessageForm(request.POST)
    if form.is_valid():
            message = form.save()
            message.user_id = user_id
            message.chat_id = current_chat.id
            message.save()
            current_chat.last_message = message.content
            current_chat.save() 
            return JsonResponse({
                'Message' : 'Messahe has been added',
            })
    else:
            return JsonResponse({'Error': form.errors}, status=-400)


@require_http_methods(['GET'])
def get_message_list (request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    user_id = 1
    try:
        user = User.objects.filter(id=int(user_id))[0]
    except ValueError:
        user = []
    if not user:
        return JsonResponse({'response': 'no such users {}'.format(user_id)})

    chat_messages = Message.objects.filter(chat_id=pk).values()
    if not chat_messages:
        return JsonResponse({'Error':'Messages for Chat#{} not found'.format(pk)})
    response = {
        'chat': pk,
        'user': user.username,
        'messages' : [{
            'content': message.get('content'),
            'date': message.get('date'),
        }for message in chat_messages]
    }  

    return JsonResponse(response)

@csrf_exempt
@require_http_methods(['POST'])
def readed_messages(request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    user_id = request.POST['user_id']
    date = datetime.datetime.now()
    messages = Message.objects.filter(chat_id=pk).filter(user_id = user_id).filter(date__lte=date)
    for message in messages:
        message.is_readed = True
        message.save()
    return JsonResponse({'Messages': 'readed'})

