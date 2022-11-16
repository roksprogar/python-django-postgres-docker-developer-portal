from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .utils import searchProfiles

def loginUser(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.add_message(request, messages.ERROR, 'Username doesn\'t exist!')
        
        # For valid credentials, we get an User or None
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log in the user (creates a session, returns as a browser cookie)
            login(request, user)
            return redirect('profiles')
        
        messages.add_message(request, messages.ERROR, 'Username or password is incorrect!')
    
    context = {'page': page}
    return render(request, 'users/login-signup.html', context)

def logoutUser(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'User was successfully logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # Create a User model instance, but don't save to the db yet.
            user.username = user.username.lower()
            user.save()

            messages.add_message(request, messages.SUCCESS, 'User was successfully created!')
            login(request, user) # Creates a session in the table and the cookie and logs in the user.
            return redirect('edit_account')

        messages.add_message(request, messages.ERROR, 'Entered information is invalid!')

    context = {'page': page, 'form': form}
    return render(request, 'users/login-signup.html', context)

def profiles(request):
    profiles, search_query = searchProfiles(request)
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profile-list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    
    # Get all skills that have a description (exclude all with empty string descriptions)
    topSkills = profile.skill_set.exclude(description__exact="")

    # Get the rest of the skills (that have an empty string for a description).
    otherSkills = profile.skill_set.filter(description="")
    
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/profile-single.html', context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    
    # Get all skills that have a description (exclude all with empty string descriptions)
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    context={'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/profile-account.html', context)

@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    
    context = {'form': form}
    return render(request, 'users/profile-form.html', context)

@login_required(login_url="login")
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.add_message(request, messages.SUCCESS, 'A new skill was created!')
            return redirect('account')
    
    context = {'form': form}
    return render(request, 'users/skill-form.html', context)

@login_required(login_url="login")
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk) # Ensure only owned skills can be edited.
    form = SkillForm(instance=skill)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'A skill was updated!')
            return redirect('account')
    
    context = {'form': form}
    return render(request, 'users/skill-form.html', context)

def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    
    if request.method == 'POST':
        skill.delete()
        messages.add_message(request, messages.SUCCESS, 'A skill was removed!')
        return redirect('account')
    
    context = {'object': skill}
    return render(request, 'delete_confirm.html', context)
    