from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Profile

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
            return redirect('profiles')

        messages.add_message(request, messages.ERROR, 'Entered information is invalid!')

    context = {'page': page, 'form': form}
    return render(request, 'users/login-signup.html', context)

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