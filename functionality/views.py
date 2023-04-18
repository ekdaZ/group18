from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def timetable(request):
    user = User.objects.get(username = request.user.username)
    try:
        activity_obj = Activity.objects.get(user_id = user)
    except:
        activity_obj = None
    context = {'activity': activity_obj}
    return render(request, 'timetable.html',context)

def info(request):
    return render(request, 'info.html')
