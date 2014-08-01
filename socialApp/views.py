from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from socialEngine.forms import ProfileForm
from django.contrib.auth.models import User
from socialApp.models import Pub, Profile
from django.template import loader, Context, RequestContext

@login_required(login_url='/login/')
def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def log_in(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def log_out(request):
    logout(request)
    return render_to_response('logout.html', context_instance=RequestContext(request))

def auth_view(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = authenticate(username=email,password=password)
    #return HttpResponse(user)
    if user is not None:
        login(request, user)
        return render_to_response('home.html', context_instance=RequestContext(request))
        #return render('hay un usuario')
    else:
        return render_to_response('error_login.html', context_instance=RequestContext(request))
        #return render('no hay usuario')
        
def error_login(request):
    return render_to_response('error_login.html', context_instance=RequestContext(request))
    
def follows(request):
    return render_to_response('follows.html', context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('register_success.html', context_instance=RequestContext(request))

def register_user(request):
    if request.POST:
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password1', '')
        if password1 == password2:
            new_user = User(username=email,email=email)
            new_user.set_password(password1)
            new_user.save()
            new_profile = Profile(user=new_user,
                                  email=email,
                                  firstName=request.POST.get('firstName', ''),
                                  lastName=request.POST.get('lastName', ''),
                                  birth_date=request.POST.get('birth_date', ''),
                                  sex=request.POST.get('sex', ''))
            new_profile.save()
            return render_to_response('home.html', context_instance=RequestContext(request))
        else:
            return render_to_response('error_login.html', context_instance=RequestContext(request))
    else:
        form = ProfileForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    
    return render_to_response('register.html',args)

@login_required(login_url='/login/')
def wall(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    p=Profile.objects.get(id=offset)
    wall_pubs=p.pub_set.all()
    template = loader.get_template("wall.html")
    context = RequestContext(request,{'wall_pubs':wall_pubs})
    return HttpResponse({template.render(context)})

@login_required(login_url='/login/')
def show_profiles(request):
    profile_list=Profile.objects.all()
    template = loader.get_template("profile_list.html")
    context = RequestContext(request,{'profile_list':profile_list})
    return HttpResponse({template.render(context)})
