from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView),
    path('tests/<str:level>/', views.QuestionsView, name='questions')
]