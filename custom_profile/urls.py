from django.urls import path, include

from custom_profile.views import profile_view, ProfileUpdateView

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/<int:id>/update/', ProfileUpdateView.as_view(), name='profile_update')
]