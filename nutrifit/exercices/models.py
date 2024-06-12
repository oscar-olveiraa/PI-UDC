from django.db import models
from django.contrib.auth.models import User

class Ejercicio(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intensity = models.CharField(max_length=25)
    muscles = models.CharField(max_length=25)
    day = models.CharField(max_length=15)
    sets = models.IntegerField(default=3) 
    reps_min = models.IntegerField(default=8) 
    reps_max = models.IntegerField(default=12) 
    workout = models.CharField(max_length=100, default='null') 

