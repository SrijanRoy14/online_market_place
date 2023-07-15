from django.shortcuts import render,redirect
from item.models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.
def index(request):
    items=item.objects.filter(is_sold=False)[0:6]
    categories=category.objects.all()
    return render(request,'core/index.html',{'categories':categories,'items':items})

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method=='POST':
        form=signupform(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:           
        form=signupform()
    return render(request,'core/signup.html',{'form':form})

def log_user(request):
    logout(request)
    messages.success(request,"You were logged out successfully, Please log in to your account!")
    return redirect('core:index')