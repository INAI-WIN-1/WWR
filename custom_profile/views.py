from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from custom_profile.models import Game, Profile

# def rating_list(request):
#     profiles = Profile.objects.all()
#     return render(request, 'ratings.html', {'profiles': profiles})

@login_required
def profile_view(request):
    user = request.user
    games = Game.objects.filter(user=user)
    return render(request, 'profile.html', {'games': games})
