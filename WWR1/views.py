from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView, DetailView, ListView
import random
class IndexView(View):
    def get(self, request):
        words = ['hello', 'Halo', 'Konnichiwa', 'Nihao',
                 'Privet', 'Hola', 'Arriva', 'Oneo-haseyo', 'Bonjur']
        word = random.choice(words)
        return render(request, 'main.html', {'app': word} )