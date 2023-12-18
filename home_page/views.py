from django.shortcuts import render

from home_page.models import HomePage

def homePageView(request):
    if request.method == "GET":
        content = HomePage.objects.first()
        return render(request, template_name='home_page.html', context={'content': content})

