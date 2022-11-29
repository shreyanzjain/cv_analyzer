from django.shortcuts import render
from .forms import UserForm
from .models import UserUploads

import app1
# Create your views here.

def homeUrl(request,*args,**kwargs): #arguments and keyword arguments
    # print(request.user)
    # print(args,kwargs)
    # return HttpResponse("<h1> Hello World </h1>")
    lst = app1.conform()
    # print("string:" , df.to_html)
    return render(request, 'home.html', {'val': lst})

def contactURl(request,*args,**kwargs):
    # return HttpResponse("<h1>Contact</h1>")
    return render(request, 'contact.html', {})

def user_upload(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    value = app1.conform()
    homeuri = homeUrl(request)
    context = {
        'form': form,
        'value': value,
        'homeuri': homeuri
    }
    print(request.POST)
    return render(request, 'create.html', context)

def user_login(request):
    return render(request, 'login.html', {})

def user_signup(request):
    return render(request, 'signup.html', {})