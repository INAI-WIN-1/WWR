from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from custom_profile.models import CustomUser


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
