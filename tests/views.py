import random
from django.shortcuts import render, get_object_or_404, redirect

from custom_profile.models import Game, Profile
from tests.models import Test


# views.py

from django.shortcuts import render
from custom_profile.models import Profile

# def indexView(request):
#     if request.user.is_authenticated:
#         cuser = request.user
#         try:
#             cuser_profile = Profile.objects.get(user=cuser)
#         except Profile.DoesNotExist:
#             cuser_profile = None
#         profiles = Profile.objects.all().order_by('-balance')
#         ranked_profiles = [(index + 1, profile) for index, profile in enumerate(profiles)]
#         return render(request, template_name='index.html', context={'ranked_profiles': ranked_profiles, 'cuser_profile': cuser_profile})
#     else:
#         profiles = Profile.objects.all().order_by('-balance')
#         ranked_profiles = [(index + 1, profile) for index, profile in enumerate(profiles)]
#         return render(request, template_name='index.html', context={'ranked_profiles': ranked_profiles, 'cuser_profile': None})
# views.py

from django.shortcuts import render
from custom_profile.models import Profile


def indexView(request):
    if request.user.is_authenticated:
        cuser = request.user
        try:
            cuser_profile = Profile.objects.get(user=cuser)
        except Profile.DoesNotExist:
            cuser_profile = None
        profiles = Profile.objects.all().order_by('-balance')
        cuser_rank = list(profiles).index(cuser_profile) + 1 if cuser_profile else None
        ranked_profiles = [(index + 1, profile) for index, profile in enumerate(profiles)]
        return render(request, template_name='index.html',
                      context={'ranked_profiles': ranked_profiles, 'cuser_profile': cuser_profile,
                               'cuser_rank': cuser_rank})
    else:
        return render(request, template_name='index.html',
                      context={'ranked_profiles': [], 'cuser_profile': None, 'cuser_rank': None})


ratings_by_level = {
    'EASY': [500, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000],
    'MEDIUM': [5000, 10000, 15000, 25000, 50000, 100000, 150000, 200000, 300000, 400000],
    'HARD': [50000, 100000, 150000, 200000, 300000, 400000, 600000, 800000, 1000000, 3000000]
}

def create_game (user, status, rating):
    if user.is_authenticated:
        game = Game.objects.create(
            user=user,
            status=status,
            rating=rating,
        )

def update_balance (user, rating):
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        profile.balance += rating
        profile.save()


def QuestionsView(request, level, id):
    level = level.upper()
    ratings = ratings_by_level[level]
    index = id - 1
    rating = ratings[id - 1]
    user = request.user
    if request.method == "GET":
        chosen_tests = request.session.get('chosen_tests', [])
        completed_questions = request.session.get('completed_questions', 0)

        if not chosen_tests:
            tests = list(Test.objects.filter(level=level))

            if len(tests) >= 10:
                selected_tests = random.sample(tests, 10)
            else:
                selected_tests = random.sample(tests, len(tests))

            chosen_tests = [{'id': test.id, 'question': test.question, 'answers': test.answers.split(', '), 'correct_answer': test.correct_answer} for test in selected_tests]
            request.session['chosen_tests'] = chosen_tests

        if id != completed_questions + 1:
            return redirect('questions', level=level, id=completed_questions+1)

        if len(chosen_tests) < id:
            request.session['chosen_tests'] = []
            request.session['completed_questions'] = 0
            create_game(user, True, rating)
            update_balance(user, rating)
            return render(request, 'tests.html', {'finish_game': True, 'id': index, 'rating': rating})
        test = chosen_tests[id-1]

        return render(request, 'tests.html', {'test': test, 'id': id, 'rating': rating})

    elif request.method == "POST":
        finish_game = request.POST.get('finish_game')
        time_lost = request.POST.get('time_lost')

        if time_lost:
            request.session['chosen_tests'] = []
            request.session['completed_questions'] = 0
            create_game(user, False, rating)
            return render(request, 'tests.html', {'level': level, 'id': id, 'wrong_answer': True, 'rating': rating})

        if finish_game:
            request.session['chosen_tests'] = []
            request.session['completed_questions'] = 0
            create_game(user, True, ratings[id-2])
            update_balance(user, ratings[id-2])
            return render(request, 'tests.html', {'finish_game': True, 'id': index, 'rating': ratings[id - 2]})
        selected_test = request.POST.get('selected_test')
        selected_answer, correct_answer = selected_test.split('|')

        if selected_answer == correct_answer:
            if id == 10:
                request.session['chosen_tests'] = []
                request.session['completed_questions'] = 0
                create_game(user, True, ratings[9])
                update_balance(user, ratings[9])
                return render(request, 'tests.html', {'win_game': True, 'level': level.lower(),'id': index, 'rating': ratings[9]})
            request.session['completed_questions'] = id
            next_id = id + 1
            return redirect('questions', level=level, id=next_id)
        else:
            request.session['chosen_tests'] = []
            request.session['completed_questions'] = 0
            create_game(user, False, rating)
            return render(request, 'tests.html', {'level': level, 'id': id, 'wrong_answer': True, 'rating': rating})