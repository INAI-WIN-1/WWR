from django.shortcuts import render

from home_page.models import HomePage

def indexView(request):
    if request.method == "GET":
        content = HomePage.objects.all()
        return render(request, template_name='home_page.html', context={'content': content[0]})

