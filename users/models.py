from django.db import models
from django.contrib.auth.models import User




class CustomUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=30, default='')

    def __str__(self) -> str:
        name = self.firstname + ' ' + self.surname
        return name