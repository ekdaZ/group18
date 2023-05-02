from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required





from .models import *


def register(request):
    auth_form = UserCreationForm()
    form = CustomUserForm()
    if request.method == "POST":
        auth_form = UserCreationForm(request.POST)
        form = CustomUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('surname')
            gndr = form.cleaned_data.get('gender')

        if auth_form.is_valid():
            user_login = auth_form.cleaned_data['username']
            try:
                holder = User.objects.get(username = user_login)
            except:
                holder = None
            if holder == None:
                user = auth_form.save()
                CustomUser.objects.create(
                        user = user,
                        firstname = name,
                        surname = lastname,
                        gender = gndr
                )
                


                return redirect('login')
            else:
                messages.info(request, "Login already exists")

    context = {'form':form , 'auth': auth_form}
    return render(request, 'register.html',context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username,password = password )

        if user is not None:
            login(request, user)
            return redirect('info')
        else:
            messages.info(request, "Username or password is incorrect")
    context = {}
    return render(request, 'login.html',context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('info')