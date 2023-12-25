from django.urls import path, include
from auth.views import UserCreateView
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('signup/',UserCreateView.as_view(), name='signUp'),
    # path('signin/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),
]