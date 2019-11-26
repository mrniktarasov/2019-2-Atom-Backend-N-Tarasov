from django import forms
from .models import Message, Chat

class MessageForm (forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content', 'date')

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
    