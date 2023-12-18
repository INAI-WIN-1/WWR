from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from custom_profile.models import Game


@login_required
def profile_view(request):
    id = request.user.id

    try:
        user = User.objects.get(id=id)
        games = Game.objects.filter(user=user)

    except User.DoesNotExit:
        games = []

    return render(request, 'profile.html', {'games': games})
