from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView
from auth.forms import UserSignUpForm
from django.urls import reverse_lazy

class UserCreateView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('main')
    template_name ='authLayOut/registr.html'
