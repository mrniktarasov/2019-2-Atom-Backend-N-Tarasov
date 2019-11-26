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
        current_chat = Chat.objects.filter(id=pk).first()
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
    user_id = request.POST['id']
    try:
        user = User.objects.filter(id=user_id).first()
    except:
        user = None
    if user is None:
        return JsonResponse({'Error': 'Invvalid user {}'.format(user_id)})
    form = CreatePersonalChat(request.POST)
    if form.is_valid(): 
        chat = form.save()
        chat.topic = 'Personal chat'
        chat.user.add(user_id)
        chat.save()
        return JsonResponse({'Create_personal_chat': 'Personal chat has been created'})
    return JsonResponse({'Errors' : form.errors}, status=400)

@require_http_methods(['GET','POST'])
def get_chat_list(request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    try:
        user = User.objects.filter(id=pk).first()
    except:
        user = None
    if  not user:
        return JsonResponse({'Error': 'Invalid user {}'.format(pk)}, status=400)
    chats = Chat.objects.filter(user=pk).values()
    if not chat:
        return JsonResponse({'Error': 'User has no chats'}, status=400)

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
    current_chat = Chat.objects.filter(id=pk).first()
    if not current_chat:
        return JsonResponse({'Error':'Chat#{} not found'.format(pk)}, status=400)
    user_id = request.POST['user_id']
    try:
        user = User.objects.filter(id=user_id).first()
    except User.DoesNotExist:
        return JsonResponse({'Error': 'No such objects'}, status=404)
 
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
            return JsonResponse({'Error': form.errors}, status=400)


@require_http_methods(['GET'])
def get_message_list (request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'})
    user_id = request.GET['user_id']
    try:
        user = User.objects.filter(id=user_id).first()
    except User.DoesNotExist:
        user = None
    if not user:
        return JsonResponse({'response': 'no such users {}'.format(user_id)}, status=404)

    chat_messages = Message.objects.filter(chat_id=pk).values()
    if not chat_messages:
        return JsonResponse({'Error':'Messages for Chat#{} not found'.format(pk)}, status=404)
    response = {
        'chat': pk,
        'user': user.username,
        'messages' : [{
            'content': message.get('content'),
            'date': message.get('date'),
            'is_read': message.get('is_read')
        }for message in chat_messages]
    }  

    return JsonResponse(response)

@csrf_exempt
@require_http_methods(['POST'])
def readed_messages(request, pk=None):
    if(pk is None):
        return JsonResponse({'Error': 'ID is None'}, status=400)
    user_id = request.POST['user_id']
    try:
        user = User.objects.filter(id=user_id).first()
    except User.DoesNotExist:
        user = None
    if not user:
        return JsonResponse({'response': 'no such users {}'.format(user_id)}, status=404)
    try:
        chat = Chat.objects.filter(id=pk).first()
    except Chat.DoesNotExist:
        chat = None
    if chat is None:
        return JsonResponse({'Error': 'Chat#{} does not find'.format(pk)}, status=404)
    last_read_message_id = user.last_read_message 
    try:
        message_last = Message.objects.filter(id_gte=last_read_message_id).last()
    except Message.DoesNotExist:
        return JsonResponse({'All meesages': 'read'})
    user.last_read_message = message_last
    user.save()

    return JsonResponse({'Messages': 'have been read'})

