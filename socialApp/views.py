from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from socialApp.models import Pub, Profile
from django.template import loader, Context

@login_required(login_url='/login/')
def home(request):
    return render_to_response('home.html')

def log_in(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def log_out(request):
    logout(request)
    return render_to_response('logout.html')

def auth_view(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = authenticate(username=email,password=password)
    #return HttpResponse(user)
    if user is not None:
        login(request, user)
        return render_to_response('home.html')
        #return render('hay un usuario')
    else:
        return render_to_response('error_login.html')
        #return render('no hay usuario')
        
def error_login(request):
    return render_to_response('error_login.html')
    
def follows(request):
    return render_to_response('follows.html')

def register_user(request):
    print request
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')
    args = {}
    args.update(csrf(request))
    
    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')
    
def wall(request):
    p=Profile.objects.get(id=1)
    wall_pubs=p.pub_set.all()
    template = loader.get_template("wall.html")
    context = Context({'wall_pubs':wall_pubs})
    return HttpResponse({template.render(context)})
