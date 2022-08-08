from django.shortcuts import render

# Create your views here.
def profiles(request):
    return render(request, 'profiles/profiles.html')

def profile(request):
    return render(request, 'profiles/profile.html')

def newProfile(request):
    return render(request, 'profiles/newProfile.html')

def login(request):
    return render(request, 'dashboard/login.html')

