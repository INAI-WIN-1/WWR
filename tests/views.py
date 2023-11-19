import random
from django.shortcuts import render, get_object_or_404, redirect
from tests.models import Test


def indexView(request):
    if request.method == "GET":
        return render(request, template_name='index.html', context={'posts': 'hello from tests'})


def QuestionsView(request, level, id):
    if request.method == "GET":
        tests = Test.objects.filter(level=level.upper())
        asked_questions = request.session.get('asked_questions', [])
        print(asked_questions)

        available_tests = [test for test in tests if test.id not in asked_questions]

        if not available_tests:
            request.session['asked_questions'] = []
            return render(request, 'tests.html', {'finish_game': True, 'id': id - 1})

        test = random.choice(available_tests)
        test.answers = test.answers.split(', ')
        asked_questions.append(test.id)
        request.session['asked_questions'] = asked_questions
        return render(request, 'tests.html', {'test': test, 'id': id})

    elif request.method == "POST":
        finish_game = request.POST.get('finish_game')
        print(finish_game)
        if finish_game:
            request.session['asked_questions'] = []
            # здесь будет логика зачисления денег на баланс пользователя
            return render(request, 'tests.html', {'finish_game': True, 'id': id - 1})
        selected_test = request.POST.get('selected_test')
        selected_answer, correct_answer = selected_test.split('|')

        if selected_answer == correct_answer:
            next_id = id + 1
            return redirect('questions', level=level, id=next_id)
        else:
            request.session['asked_questions'] = []
            return render(request, 'tests.html', {'level': level, 'id': id, 'wrong_answer': True})
