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
from django.http import JsonResponse
from .utils import lipa_na_mpesa_online

def initiate_payment(request):
    phone_number = request.GET.get('phone')
    amount = request.GET.get('amount')
    account_reference = 'your_account_reference'
    transaction_desc = 'Payment Description'
    callback_url = 'https://your_domain.com/payments/callback'
    
    response = lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc, callback_url)
    return JsonResponse(response)
    

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
        # brands=cars.brand.all()
    # cars = Car.objects.all()
    context={"cars":cars}
    return render(request,"carbooking/home.html",context)



def Detail(request,pk):
    cars=Car.objects.get(id=pk)
    brands=cars.brand.all()
    context={"cars":cars,"brands":brands}
    return render(request,"carbooking/detail.html",context)

def Hire(request):

    
    context={}
    return render(request,"carbooking/hire.html",context)

@login_required
def Logout(request):
    logout(request)
    
    return redirect("home")

def Status():
    pass
    
    
