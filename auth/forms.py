from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserSignUpForm(UserCreationForm):
    mail = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'mail',
            'password1',
            'password2',
        ]
