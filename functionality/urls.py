from django.urls import path
from . import views

urlpatterns = [
    path('timetable/', views.timetable, name = 'timetable'),
    path('', views.info, name= "info"),
    path('create-activity/', views.new_activity, name = 'new-activity')
]