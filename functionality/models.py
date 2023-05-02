from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Activity(models.Model):
    activity_name = models.CharField(max_length = 200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_start = models.DateField()
    # date_time_finish = models.DateTimeField()
    duration = models.IntegerField(default=1)
    completion = models.DecimalField(decimal_places=3, max_digits=4, default=0)
    # date_time_added = models.DateField()
    record_description = models.CharField(max_length=2000)
    def __str__(self):
        return self.activity_name
    
class SubActivity(models.Model):
    activity_ref  = models.ForeignKey(Activity, on_delete=models.CASCADE)
    duration = models.DecimalField(decimal_places=3, max_digits=4, default=0)
    booster = models.CharField(max_length=50)
    date = models.DateField()