from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profile-list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    
    # Get all skills that have a description (exclude all with empty string descriptions)
    topSkills = profile.skill_set.exclude(description__exact="")

    # Get the rest of the skills (that have an empty string for a description).
    otherSkills = profile.skill_set.filter(description="")
    
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/profile-single.html', context)