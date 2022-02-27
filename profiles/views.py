from django.shortcuts import render, get_object_or_404

from .models import Profile
from .forms import ProfileForm

# Create your views here.

def profiles(request):
    """
    dlkcvjadl
    """
    model = Profile
    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(instance=profile)


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, template, context)

