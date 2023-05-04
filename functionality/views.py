from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ActivityForm
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
import csv

# Create your views here.

@login_required(login_url='login')
def timetable(request):
    user = User.objects.get(username = request.user.username)
    try:
        activity_obj = Activity.objects.filter(user_id = user)
    except:
        activity_obj = None
    context = {'activity': activity_obj}
    return render(request, 'timetable.html',context)

def info(request):
    return render(request, 'info.html')

@login_required(login_url='login')
def new_activity(request):
    form = ActivityForm()
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('activity_name')
            duration = form.cleaned_data.get('duration')
            description = form.cleaned_data.get('record_description')
            # end = form.cleaned_data.get('date_time_finish')
            start = form.cleaned_data.get('date_time_start')
            now = datetime.datetime.today()
            start = start.replace(tzinfo = None)
            # end = end.replace(tzinfo = None)
            user = User.objects.get(username = request.user.username)
            if now <= start:
                Activity.objects.create(
                    activity_name = name,
                    user_id = user,
                    date_time_start = start,
                    # date_time_finish = end,
                    duration = duration,
                    completion = 0,
                    record_description = description,
                    # date_time_added = now
                )
            else:
                messages.info(request, "Start date before due and start date after current date")

    context = {'form': form}
    return render(request, 'create-activity.html' , context)


@login_required(login_url='login')
def timer(request, activity_name):
    activity = Activity.objects.get(activity_name = activity_name)
    time = int((activity.duration*3600 - activity.completion*3600) // 1)
    context = {'time': time}
    return render(request, "timer.html", context)
    
@login_required(login_url='login')
def graph(request,activity_name):
        records = SubActivity.objects.filter(activity_name = activity_name).order_by("-date")
        with open('storage.csv', mode ='w', newline='') as results:
            results_writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(["Duration:"] + records.duration)
            results_writer.writerow(["Booster:"] + records.booster)
            results_writer.writerow(["Date"] + records.date)


