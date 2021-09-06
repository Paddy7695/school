from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import models
from django.contrib.auth.models import User
from .models import *
from django import forms


class signupform (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']




class userlogin_form (AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


