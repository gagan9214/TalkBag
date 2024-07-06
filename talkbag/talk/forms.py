from django import forms
from .models import Talk
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class talkForm(forms.ModelForm):
    
    class Meta:
        model = Talk
        fields = ['text','photo']

class userRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model= User
        fields=('username','email','password1','password2')
