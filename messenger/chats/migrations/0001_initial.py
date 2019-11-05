# Generated by Django 2.2.5 on 2019-11-02 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_group_chat', models.BooleanField(default=False, null=True)),
                ('topic', models.CharField(default='Chat', max_length=64)),
                ('last_message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('date', models.CharField(default='16:00', max_length=16)),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.Chat')),
            ],
        ),
    ]
