from django.shortcuts import render,redirect
from . models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Login(request):
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    else:
        form=LoginForm()
    return render(request,"carbooking/login.html",{"form":form})

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Account created {username}")
            return redirect('login')
    else:
            form=RegisterForm()
    return render(request,"carbooking/register.html",{"form":form})



def Home(request):
    query=request.GET.get('q')

    if query:
        cars=Car.objects.filter(name__icontains=query)
    else:
        cars = Car.objects.all() 
    # cars = Car.objects.all()
    context={"cars":cars}
    return render(request,"carbooking/home.html",context)



def Detail(request,pk):
    cars=Car.objects.get(id=pk)
    context={"cars":cars}
    return render(request,"carbooking/detail.html",context)


def Logout(request):
    logout(request)
    
    return redirect("home")


# def search(request):
#     query=request.GET.get('q')
#     if query:
#         results=Car.objects.filter(name__icontains=query)
#         return render(request,"carbooking/search.html",{"results":results})
#     else:
#         return render(request,"carbooking/search.html",{"results":None})
