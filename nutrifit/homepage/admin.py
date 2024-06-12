from django.contrib import admin
from .models import UsuarioApp, Historico, Historico_micronutrientes
# Register your models here.

@admin.register(UsuarioApp)
class UsuarioAppAdmin(admin.ModelAdmin):
    list_display = ('user', 'sexo', 'estatura', 'edad', 'peso_origen','peso_act', 'peso_des', 'nivel_actividad')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'tdee', 'peso')

@admin.register(Historico_micronutrientes)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'calcium', 'chromium', 'copper', 'fluoride', 'iodine', 'iron', 'magnesium', 'manganese', 'molybdenum', 'phosphorus', 'selenium', 'zinc', 'potassium', 'sodium', 'chloride')


