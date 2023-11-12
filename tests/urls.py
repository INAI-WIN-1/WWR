from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView),
    path('tests/<id>/', views.QuestionsView, name='questions by level')
]