from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView
from auth.forms import UserSignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def my_view(request):
    print(request.session)
    user_data = {
        'username': request.user.username,
        'email': request.user.email,
        'is_authenticated': request.user.is_authenticated,
    }
    return render(request, 'index.html', {'user_data': user_data})


class UserCreateView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('home')
    template_name ='authLayOut/registr.html'



# class CustomLoginView(LoginView):
#     template_name = 'authLayOut/login.html'
#
#     def get_success_url(self):
#         return reverse_lazy('main')

@login_required
def profile_view(request):
    return render(request, 'profile.html')