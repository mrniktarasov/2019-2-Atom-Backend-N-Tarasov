from django.db import models

class Chat (models.Model):
    user = models.ManyToManyField('users.User')
    is_group_chat = models.BooleanField('Группа',null=True, default=False)
    topic = models.CharField('Заголовок',max_length=64, default='Chat')
    last_message = models.TextField('Последнее сообщение',default='')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message (models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    content = models.TextField('Содержание',default='')
    date = models.DateTimeField('Дата', auto_now_add=True)
    image = models.ImageField(upload_to='image/', null=True)
    image_key = models.TextField('Ключ для изображения', default='')
    image_mime_type = models.TextField('MIME тип изображения', default='')


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-date']

