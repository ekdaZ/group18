from django.urls import path
from . import views

urlpatterns = [
    path('timetable/', views.timetable, name = 'timetable'),
    path('', views.info, name= "info"),
    path('create-activity/', views.new_activity, name = 'create-activity'), 
    path('timer/<str:activity_name>/', views.timer, name = 'timer'),
    path('overview/', views.overview, name = 'overview'),
    path('stop/', views.timer_stop, name='timer_stop'),
]