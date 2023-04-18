from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    activity_name = models.CharField(max_length = 200)
    user_id = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    date_time_start = models.DateTimeField()
    date_time_finish = models.DateTimeField()
    date_time_added = models.DateTimeField()
    record_description = models.CharField(max_length=2000)

    def __str__(self):
        return self.activity_name