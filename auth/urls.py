from django.urls import path, include
from auth.views import UserCreateView, profile_view
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('signup/',UserCreateView.as_view(), name='signUp'),
    # path('signin/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
]