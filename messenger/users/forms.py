from django  import forms
from .models import User

class searchUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'avatar', 'last_read_message')
