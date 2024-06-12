from django.urls import path

from . import views

urlpatterns = [
    path('', views.rutina, name='misrutinas'),
    path('ejercicios/', views.ver_ejercicios, name='misejercicios'),
    path('editarutina/<int:ejercicio_id>/', views.editar_rutina, name='editarutina'),
    path('eliminarutina/<int:ejercicio_id>/', views.eliminar_rutina, name='eliminarutina'),
]