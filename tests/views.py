from django.shortcuts import render

from tests.models import Test


def indexView(request):
    if request.method == "GET":
        return render(request, template_name='index.html', context={'posts': 'hello from tests'})


def QuestionsView(request, level):
    if request.method == "GET":
        tests = Test.objects.filter(level=level.upper())
        for test in tests:
            test.answers = test.answers.split(', ')
        return render(request, 'tests.html', {'tests': tests})
