from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Message, ReadedMessage
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from .forms import MessageForm, CreatePersonalChat
from django.core.files.images import ImageFile
import magic
from django.contrib.auth.decorators import login_required

@login_required
@require_http_methods(['GET', 'POST'])
def chat (request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'})
    current_chat = Chat.objects.filter(id=chat_id).first()
    return JsonResponse({
        'is group chat': current_chat.is_group_chat,
        'topic': current_chat.topic,
        'last message': current_chat.last_message,
    })
    
@login_required
@csrf_exempt
@require_http_methods(['POST'])
def create_personal_chat (request):
    user = request.user
    topic = request.POST.get('topic')
    form = CreatePersonalChat(request.POST)
    if form.is_valid(): 
        chat = form.save()
        chat.topic = topic
        chat.user.add(user.id)
        chat.save()
        readedMessage = ReadedMessage.objects.create()
        readedMessage.user_id = user.id
        readedMessage.chat_id = chat.id
        readedMessage.save()
        return JsonResponse({'Create_personal_chat': 'Personal chat has been created'})
    return JsonResponse({'Errors' : form.errors}, status=400)

@login_required
@require_http_methods(['GET','POST'])
def get_chat_list(request):
    user = request.user 
    chats = Chat.objects.filter(user=user.id).values()
    if not chat:
        return JsonResponse({'Error': 'User has no chats'}, status=400)

    response = {
        'name': user.name,
        'username': user.username,
        'usernick': user.nick,
        'user id': user.id,
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

@login_required
@csrf_exempt
@require_http_methods(['POST'])
def add_message(request, chat_id=None):
    content = request.POST.get('content')
    user = request.user
    if chat_id is None:
        return JsonResponse({'Error': 'invalid chat {}'.format(chat_id)}, status=400)
    current_chat = Chat.objects.filter(id=chat_id).first()
    if not current_chat:
        return JsonResponse({'Error':'Chat#{} not found'.format(chat_id)}, status=400)

    form = MessageForm(request.POST)
    if form.is_valid():
            message = form.save()
            message.content = content
            message.user_id = user.id
            message.chat_id = current_chat.id
            message.save()
            current_chat.last_message = message.content
            current_chat.save() 
            return JsonResponse({
                'Message' : 'Messahe has been added',
            })
    else:
            return JsonResponse({'Error': form.errors}, status=400)

@login_required
@require_http_methods(['GET'])
def get_message_list (request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'})
    user = request.user

    chat_messages = Message.objects.filter(chat_id=chat_id).values()
    if not chat_messages:
        return JsonResponse({'Error':'Messages for Chat#{} not found'.format(chat_id)}, status=404)
    response = {
        'chat': chat_id,
        'user': user.username,
        'messages' : [{
            'content': message.get('content'),
            'date': message.get('date'),
            'id': message.get('id')
        }for message in chat_messages]
    }  

    return JsonResponse(response)

@login_required
@csrf_exempt
@require_http_methods(['POST'])
def read_messages(request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'}, status=400)
    user = request.user
    chat = Chat.objects.filter(id=chat_id).first()
    if chat is None:
        return JsonResponse({'Error': 'Chat#{} does not find'.format(chat_id)}, status=404)
    last_read_message = ReadedMessage.objects.filter(user_id=user.id).filter(chat_id=chat_id).first()
    message_last = Message.objects.filter(user_id=user.id).filter(chat_id=chat_id).filter(id__gte=last_read_message.last_read_message).last()
    if message_last is None:
        return JsonResponse({'All meesages': 'read'})
    last_read_message.last_read_message = message_last.id + 1
    last_read_message.save()
    return JsonResponse({'Response': 'Messages read {}'.format(last_read_message.last_read_message)})
