from django.urls import path
from .views import ShowProfilePageView
from django.contrib import admin

urlpatterns = [
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('admin/', admin.site.urls),
]
