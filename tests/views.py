import random
from django.shortcuts import render, get_object_or_404, redirect
from tests.models import Test


def indexView(request):
    if request.method == "GET":
        return render(request, template_name='index.html', context={'posts': 'hello from tests'})


def QuestionsView(request, level, id):
    if request.method == "GET":
        chosen_tests = request.session.get('chosen_tests', [])
        print(chosen_tests)

        if not chosen_tests:
            tests = list(Test.objects.filter(level=level.upper()))

            if len(tests) >= 10:
                selected_tests = random.sample(tests, 10)
            else:
                selected_tests = random.sample(tests, len(tests))

            chosen_tests = [{'id': test.id, 'question': test.question, 'answers': test.answers.split(', '), 'correct_answer': test.correct_answer} for test in selected_tests]
            request.session['chosen_tests'] = chosen_tests

        # available_tests = [test for test in tests if test.id not in chosen_tests]
        #
        if len(chosen_tests) < id:
            request.session['chosen_tests'] = []
            return render(request, 'tests.html', {'finish_game': True, 'id': id - 1})
        test = chosen_tests[id-1]

        return render(request, 'tests.html', {'test': test, 'id': id})

    elif request.method == "POST":
        finish_game = request.POST.get('finish_game')
        if finish_game:
            request.session['chosen_tests'] = []
            # здесь будет логика зачисления денег на баланс пользователя
            return render(request, 'tests.html', {'finish_game': True, 'id': id - 1})
        selected_test = request.POST.get('selected_test')
        selected_answer, correct_answer = selected_test.split('|')

        if selected_answer == correct_answer:
            next_id = id + 1
            return redirect('questions', level=level, id=next_id)
        else:
            request.session['chosen_tests'] = []
            return render(request, 'tests.html', {'level': level, 'id': id, 'wrong_answer': True})
