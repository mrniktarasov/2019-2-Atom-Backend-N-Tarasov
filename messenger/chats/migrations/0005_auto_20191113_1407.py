# Generated by Django 2.2.5 on 2019-11-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20191106_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='chat',
            name='is_group_chat',
            field=models.BooleanField(default=False, null=True, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='last_message',
            field=models.TextField(default='', verbose_name='Последнее сообщение'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='topic',
            field=models.CharField(default='Chat', max_length=64, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(default='', verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
