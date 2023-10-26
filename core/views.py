from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from item.models import *
from .forms import *

# Create your views here.
@login_required
def index(request):
    it=items.objects.filter(is_sold=False)[0:12]
    Cat=Category.objects.all()
    return render(request,'core/index.html',{'categories':Cat,'items':it})

def contact(request):
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def privacy(request):
    return render(request,'core/privacy.html')

def terms(request):
    return render(request,'core/terms.html')

def logoutUser(request):
    logout(request)
    return redirect('/login/')

def signup(request):
    if request.method== 'POST':
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=Signupform()
    return render(request,'core/signup.html',{'form':form})