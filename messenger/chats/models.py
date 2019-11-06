from django.db import models

class Chat (models.Model):
    user = models.ManyToManyField('users.User')
    is_group_chat = models.BooleanField('Group',null=True, default=False)
    topic = models.CharField('Topic',max_length=64, default='Chat')
    last_message = models.TextField('Last message',default='')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message (models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    content = models.TextField('Content',default='')
    date = models.CharField('Date',max_length=16, default='16:00')


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-date']

