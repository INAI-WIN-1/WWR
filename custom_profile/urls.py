from django.contrib.auth.views import LogoutView
from django.urls import path, include

from custom_profile.views import profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
]