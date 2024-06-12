from django.contrib import admin
from .models import Ejercicio

@admin.register(Ejercicio)
class RegistroEjercicios(admin.ModelAdmin):
    list_display = ('user', 'intensity', 'muscles', 'day', 'sets', 'reps_min', 'reps_max', 'workout')

# Register your models here.
