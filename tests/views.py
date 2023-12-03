import random
from django.shortcuts import render, get_object_or_404, redirect
from tests.models import Test


def indexView(request):
    if request.method == "GET":
        return render(request, template_name='index.html', context={'posts': 'hello from tests'})


ratings_by_level = {
    'EASY': [500, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000],
    'MEDIUM': [5000, 10000, 15000, 25000, 50000, 100000, 150000, 200000, 300000, 400000],
    'HARD': [50000, 100000, 150000, 200000, 300000, 400000, 600000, 800000, 1000000, 3000000]
}


def QuestionsView(request, level, id):
    level = level.upper()
    ratings = ratings_by_level[level]
    index = id - 1
    rating = ratings[id - 1]
    if request.method == "GET":
        chosen_tests = request.session.get('chosen_tests', [])
    
        if not chosen_tests:
            tests = list(Test.objects.filter(level=level))

            if len(tests) >= 10:
                selected_tests = random.sample(tests, 10)
            else:
                selected_tests = random.sample(tests, len(tests))

            chosen_tests = [{'id': test.id, 'question': test.question, 'answers': test.answers.split(', '), 'correct_answer': test.correct_answer} for test in selected_tests]
            request.session['chosen_tests'] = chosen_tests

        if len(chosen_tests) < id:
            request.session['chosen_tests'] = []
            return render(request, 'tests.html', {'finish_game': True, 'id': index, 'rating': rating})
        test = chosen_tests[id-1]

        return render(request, 'tests.html', {'test': test, 'id': id, 'rating': rating})

    elif request.method == "POST":
        finish_game = request.POST.get('finish_game')
        if finish_game:
            request.session['chosen_tests'] = []
            # здесь будет логика зачисления денег на баланс пользователя
            return render(request, 'tests.html', {'finish_game': True, 'id': index, 'rating': ratings[id - 2]})
        selected_test = request.POST.get('selected_test')
        selected_answer, correct_answer = selected_test.split('|')

        if selected_answer == correct_answer:
            next_id = id + 1
            return redirect('questions', level=level, id=next_id)
        else:
            request.session['chosen_tests'] = []
            return render(request, 'tests.html', {'level': level, 'id': id, 'wrong_answer': True, 'rating': rating})
