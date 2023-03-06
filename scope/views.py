
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from .models import Info,Register
from django.contrib import messages
from django.contrib.auth.models import User
# from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from project import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage,send_mail
from . import views
# from .forms import Register_Form





# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    if request.method=="POST":
        obj=Info()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()
        return redirect ("home")
    return render (request,"contact.html")

def registration(request):
    if request.method=="POST":
        obj=Register()
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        hobbies=request.POST.get('hobbies')
        
        obj.first_name=first_name
        obj.last_name=last_name
        obj.gender=gender
        obj.dob=dob
        obj.email=email
        obj.phone_number=phone_number
        obj.country=country
        obj.state=state
        obj.city=city
        obj.hobbies=hobbies
        
        obj.save()
        return redirect ("home")
    return render (request,"registration.html")





def LogoutPage(request):
    logout(request)
    return redirect('login')



# Create your views here.


