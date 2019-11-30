from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Message
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from .forms import MessageForm, CreatePersonalChat
from django.core.files.images import ImageFile
import magic

@require_http_methods(['GET', 'POST'])
def chats (request):
    return JsonResponse ({"status" : "Заглушка для списка чатов"})

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
    

@csrf_exempt
@require_http_methods(['POST'])
def create_personal_chat (request):
    if user.is_authenticated:
        topic = request.POST.get('topic') 
        form = CreatePersonalChat(request.POST)
        if form.is_valid(): 
            chat = form.save()
            chat.topic = topic
            chat.user.add(user.id)
            chat.save()
            return JsonResponse({'Create_personal_chat': 'Personal chat has been created'})
        return JsonResponse({'Errors' : form.errors}, status=400)
    else:
        return JsonResponse({'Error': 'Anonymous users do not allowed to create chats'})

@require_http_methods(['GET','POST'])
def get_chat_list(request):
    user = request.user 
    chats = Chat.objects.filter(user=user).values()
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

@csrf_exempt
@require_http_methods(['POST'])
def add_message(request, chat_id=None):
    chat_id = request.POST.get('chat_id')
    content = request.POST.get('content')
    user = request.user
    if user.is_authenticated:
        if chat_id is None:
            return JsonResponse({'Error': 'invalid chat {}'.format(chat_id)})
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
    else:
        return JsonResponse({'Error':'Anonymous users do not allowed to create chats'})


@require_http_methods(['GET'])
def get_message_list (request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'})
    user = request.user
    if not user:
        return JsonResponse({'response': 'no such users {}'.format(user_id)}, status=404)

    chat_messages = Message.objects.filter(chat_id=chat_id).values()
    if not chat_messages:
        return JsonResponse({'Error':'Messages for Chat#{} not found'.format(pk)}, status=404)
    response = {
        'chat': chat_id,
        'user': user.username,
        'messages' : [{
            'content': message.get('content'),
            'date': message.get('date'),
        }for message in chat_messages]
    }  

    return JsonResponse(response)

@csrf_exempt
@require_http_methods(['POST'])
def read_messages(request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'}, status=400)
    user = request.user
    if user.is_authenticated:
        chat = Chat.objects.filter(id=chat_id).first()
        if chat is None:
            return JsonResponse({'Error': 'Chat#{} does not find'.format(pk)}, status=404)
        last_read_message_id = user.last_read_message 
        message_last = Message.objects.filter(id__gte=last_read_message_id).last()
        if message_last is None:
            return JsonResponse({'All meesages': 'read'})
        user.last_read_message = message_last.id
        user.save()
        return JsonResponse({'Response': 'Messages read'})
    else:
        return JsonResponse({'Error': 'Anonymous users do not allowed to read messages'})

@csrf_exempt
@require_http_methods(['POST'])
def upload_file(request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'}, status=400)
    user = request.user
    if user.is_authenticated:
        im_file = request.POST.get('image')
        image_key = request.POST.get('image_key')
        chat = Chat.objects.filter(id=chat_id).first()
        if chat is None:
            return JsonResponse({'Error': 'No such Chat {}'.format(pk)}, status=404)
        mime = magic.from_file(im_file, mime=True)
        form = MessageForm(request.POST)
        if form.is_valid():
                message = form.save()
                message.user_id = user.id
                message.chat_id = chat.id
                message.image = ImageFile(open(im_file, 'rb'))
                message.image_mime_type = mime
                message.image_key = image_key
                message.save()
                chat.last_message = 'Image'
                chat.save() 
                return JsonResponse({
                    'Message' : 'Messahe has been added',
                })
        else:
                return JsonResponse({'Error': form.errors}, status=400)
    else:
        return JsonResponse({'Error': 'Anonymous users do not allowed to upload files'})

@csrf_exempt
@require_http_methods(['GET'])
def download_file(request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'}, status=400)
    image_name = request.GET.get('image_name')
    if image_name is None:
        return JsonResponse({'Error': 'invalid image key {}'.format(image_key)}, status=400)
    image_path ='/home/nikita/BackendMail/messenger/chats/images/{}'.format(image_name)
    chat = Chat.objects.filter(id=chat_id).first()
    if chat is None:
        return JsonResponse({'Error': 'No such Chat {}'.format(chat_id)}, status=404)

    image = Message.objects.filter(chat_id=chat_id).filter(image__contains=image_path).first()
    if image is None:
         return JsonResponse({'Error': 'Image with name {} have not been found'.format(image_name)}, status=404)

    return JsonResponse({'Response': 'Image {} has been found'.format(image.image.url)})

