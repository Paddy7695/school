from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform,userlogin_form
from django.contrib.auth import authenticate,login,logout
from schoolinfo import models
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def home (request):
    return render(request,'home.html')

def department (request):
    return render(request,'department.html')

def contact (request):
    return render(request,'contact.html')

def profile (request):
    user=request.user
    context={'user':user}
    return render(request,'profile.html',context)

def mech (request):
    studs = students.objects.filter(department__department_name='Mechanical')
    profs = professor.objects.filter(department__department_name='Mechanical')
    context = {'studs': studs,'profs': profs}
    return render(request,'mech.html', context)

def civil (request):
    studs = students.objects.filter(department__department_name='Civil')
    profs = professor.objects.filter(department__department_name='Civil')
    context = {'studs': studs,'profs': profs}
    return render(request,'civil.html',context)

def signup (request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            forms = signupform(request.POST)
            if forms.is_valid():
                forms.save()
                messages.info = (request,'hiiii')
                return HttpResponseRedirect('/home/')

        forms = signupform()
        context = {'forms':forms}
        return render(request,'signup.html',context)

    else:
        return HttpResponseRedirect('/profile/')


def login_form (request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            logs = userlogin_form(request,request.POST)
            if logs.is_valid():
                nam =logs.cleaned_data['username']
                passw =logs.cleaned_data['password']
                user = authenticate(username=nam,password=passw)
                login(request,user)
                messages.info = (request,'hiiii')
                return HttpResponseRedirect('/signup/')

        logs = userlogin_form()
        context = {'logs': logs}
        print('-----------------------55555555555-------------')
        return render(request,'login .html',context)

    else:
        return HttpResponseRedirect('/profile/')


def user_logout (request):
    logout(request)
    return HttpResponseRedirect('/login/')