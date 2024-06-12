from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_save

# Create your models here.
class UsuarioApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    sexo = models.CharField(max_length=10)
    estatura = models.IntegerField()    # Medido en cm
    peso_act = models.FloatField(max_length=5)      # Medido en kg
    peso_origen = models.FloatField(max_length=5)
    peso_des = models.FloatField(max_length=5)      # Medido en kg
    edad = models.IntegerField()
    nivel_actividad = models.CharField(max_length=25)



class Historico(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(unique=False)
    tdee = models.FloatField(max_length=15, unique=False) # Calorías diarias consumidas en total (TDEE en inglés). Medido en Kcal/day
    peso = models.FloatField(max_length=5)



class Historico_micronutrientes(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, unique=False)
    calcium = models.FloatField(max_length=6, unique=False)    # Medido en mg/d
    chromium = models.FloatField(max_length=5, unique=False)   # Medido en μg/d
    copper = models.FloatField(max_length=5, unique=False)     # Medido en μg/d
    fluoride = models.FloatField(max_length=5, unique=False)   # Medido en mg/d
    iodine = models.FloatField(max_length=4, unique=False)     # Medido en μg/d
    iron = models.FloatField(max_length=4, unique=False)       # Medido en mg/d
    magnesium = models.FloatField(max_length=5, unique=False)  # Medido en mg/d
    manganese = models.FloatField(max_length=4, unique=False)  # Medido en mg/d
    molybdenum = models.FloatField(max_length=4, unique=False) # Medido en μg/d
    phosphorus = models.FloatField(max_length=5, unique=False) # Medido en mg/d
    selenium = models.FloatField(max_length=4, unique=False)   # Medido en μg/d
    zinc = models.FloatField(max_length=4, unique=False)       # Medido en mg/d
    potassium = models.FloatField(max_length=6, unique=False)  # Medido en mg/d
    sodium = models.FloatField(max_length=6, unique=False)     # Medido en mg/d
    chloride = models.FloatField(max_length=6, unique=False)   # Medido en g/d