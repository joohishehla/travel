from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        Username=request.POST['Username']
        Password = request.POST['Password']
        user=auth.authenticate(username=Username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        Username = request.POST['Username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Email=request.POST['Email']
        Password = request.POST['Password']
        Password1 = request.POST['Password1']

        if Password==Password1:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=Username,password=Password,first_name=Firstname,last_name=Lastname,email=Email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not matched')
            return redirect('register')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')