from django import forms
from .models import Message, Chat

class MessageForm (forms.Form):
    content = forms.CharField(required=False)
    date = forms.DateTimeField(required=False)
    image = forms.ImageField(required=False)
    image_key = forms.CharField(required=False)
    image_mime_type = forms.CharField(required=False)

    def save(self):
        return Message.objects.create(**self.cleaned_data)
    

class CreatePersonalChat(forms.Form):
    is_group_chat = forms.BooleanField(required=False)
    topic = forms.CharField(required=False)
    last_message = forms.CharField(required=False)

    def clean_topic(self):
        if self.cleaned_data['topic'].isalpha():
            return self.cleaned_data['topic']
        return ''.join([x for x in self.cleaned_data['topic'] if x.isalpha()])
    
    def save(self):
        return Chat.objects.create(**self.cleaned_data)
    