from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def register(request):
    return render_to_response('register.html')

def login(request):
    return render_to_response('login.html')

def follows(request):
    return render_to_response('follows.html')
