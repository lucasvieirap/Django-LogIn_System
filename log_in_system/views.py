from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request, 'login.html')
