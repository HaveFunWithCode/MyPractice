from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def signup(request):
    if request.method=='POST':
        # the user want to sign up

        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'uprofile/signup.html',{'error':'Username is already taken'})
            except ObjectDoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'uprofile/signup.html',{'error':'Two password does not match'})

    else:
        # user want to enter info
        return render(request,'uprofile/signup.html')


def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'uprofile/login.html',{'error':'username or password is incorrect'})

    else:
        return render(request,'uprofile/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request,'uprofile/logout.html')