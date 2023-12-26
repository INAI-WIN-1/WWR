from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import ProfileForm
from .models import Game, Profile
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


class ProfileUpdateView(generic.UpdateView):
    template_name = "profile_update.html"
    form_class = ProfileForm
    success_url = "/profile/"

    def get_object(self, **kwargs):
        profile_id = self.kwargs.get("id")
        return get_object_or_404(Profile, id=profile_id)

    def form_valid(self, form):
        return super(ProfileUpdateView, self).form_valid(form=form)

