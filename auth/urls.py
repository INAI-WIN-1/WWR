from django.urls import path, include
from auth.views import UserCreateView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('signup/',UserCreateView.as_view(), name='signUp'),
    path('signin/',LoginView.as_view(template_name='authLayOut/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]