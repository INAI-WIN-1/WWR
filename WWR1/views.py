from django.shortcuts import render
from django.views.generic import View
import random

class IndexView(View):
    def get(self, request):
        word = 'Hello, World!'
        random_number = random.randint(1, 100)
        return render(request, 'index.html', {'app': word + f' {random_number}'})