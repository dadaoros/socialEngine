from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def home(request):
    return render_to_response('home.html')
    
def register(request):
    return render_to_response('register.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)
    
def error_login(request):
    return render_to_response('error_login.html')
    
def follows(request):
    return render_to_response('follows.html')
