from django import forms
from .models import CustomUser



class CustomUserForm(forms.Form):
    surname = forms.CharField(label='Login',max_length=100)
    firstname = forms.CharField(label='Login',max_length=100)
    gender = forms.CharField(label='Login',max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(label='Login',max_length=100)
    password1 = forms.CharField(label='Password',max_length=100)