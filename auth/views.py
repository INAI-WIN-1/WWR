from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView
from auth.forms import UserSignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


class UserCreateView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name ='authLayOut/registr.html'



# class CustomLoginView(LoginView):
#     template_name = 'authLayOut/login.html'
#
#     def get_success_url(self):
#         return reverse_lazy('main')

@login_required
def profile_view(request):
    return render(request, 'profile.html')