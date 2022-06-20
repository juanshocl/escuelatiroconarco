from urllib import request
from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
def register(request):
    return render(request, 'register/reg.html')