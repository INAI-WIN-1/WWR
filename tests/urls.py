from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='main'),
    path('tests/<str:level>/<int:id>', views.QuestionsView, name='questions')
]