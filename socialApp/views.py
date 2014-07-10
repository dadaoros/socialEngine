from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
    return render_to_response('html/register.html')

def login(request):
    return render_to_response('html/login.html')

def follows(request).
    return render_to_response('html/follows.html')
