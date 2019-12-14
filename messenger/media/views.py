from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Message
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from chats.forms import MessageForm
from django.core.files.images import ImageFile
import magic
from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
@require_http_methods(['POST'])
def upload_file(request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'}, status=400)
    user = request.user
    im_file = request.POST.get('image')
    image_key = request.POST.get('image_key')
    chat = Chat.objects.filter(id=chat_id).first()
    if chat is None:
        return JsonResponse({'Error': 'No such Chat {}'.format(chat_id)}, status=404)
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

@login_required
@csrf_exempt
@require_http_methods(['GET'])
def download_file(request, chat_id=None):
    if chat_id is None:
        return JsonResponse({'Error': 'ID is None'}, status=400)
    key = request.GET.get('key')
    if key is None:
        return JsonResponse({'Error': 'invalid image key {}'.format(key)}, status=400)
    chat = Chat.objects.filter(id=chat_id).first()
    if chat is None:
        return JsonResponse({'Error': 'No such Chat {}'.format(chat_id)}, status=404)
    message = Message.objects.filter(chat_id=chat_id).filter(image_key=key).first()
    if message is None:
         return JsonResponse({'Error': 'Image with key {} have not been found'.format(key)}, status=404)

    url = format(message.image.url)
    response = HttpResponse(url)
    response['X-Accel-Redirect'] = url
    return response
