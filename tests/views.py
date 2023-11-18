import random
from django.shortcuts import render, get_object_or_404, redirect
from tests.models import Test


def indexView(request):
    if request.method == "GET":
        return render(request, template_name='index.html', context={'posts': 'hello from tests'})


def QuestionsView(request, level, id):
    if request.method == "GET":
        tests = Test.objects.filter(level=level.upper())
        abc = 'ABCD'
        for test in tests:
            test.answers = test.answers.split(', ')
        return render(request, 'tests.html', {'test': random.choice(tests), 'id': id, 'abc': abc})

    elif request.method == "POST":
        selected_test = request.POST.get('selected_test')
        selected_answer, correct_answer = selected_test.split('|')

        if selected_answer == correct_answer:
            next_id = id + 1
            return redirect('questions', level=level, id=next_id)
        else:
            return render(request, 'tests.html', {'level': level, 'id': id, 'wrong_answer': True})
