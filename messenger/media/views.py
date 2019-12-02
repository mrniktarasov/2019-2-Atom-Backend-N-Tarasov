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
    image_name = request.GET.get('image_name')
    if image_name is None:
        return JsonResponse({'Error': 'invalid image name {}'.format(image_name)}, status=400)
    chat = Chat.objects.filter(id=chat_id).first()
    if chat is None:
        return JsonResponse({'Error': 'No such Chat {}'.format(chat_id)}, status=404)
    image_path = '/home/nikita/BackendMail/messenger/static/images/{}'.format(image_name)
    message = Message.objects.filter(chat_id=chat_id).filter(image__contains=image_path).first()
    if message is None:
         return JsonResponse({'Error': 'Image with name {} have not been found'.format(image_name)}, status=404)

    url = '/protected{}'.format(message.image)
    response = HttpResponse(url)
    response['X-Accel-Redirect'] = url
    print(url)
    print(response['X-Accel-Redirect'])
    print(response)
    return response
