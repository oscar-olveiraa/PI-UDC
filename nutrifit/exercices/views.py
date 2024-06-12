from django.shortcuts import render, redirect, get_object_or_404
from .forms import Makerutine, EditRutina
from .models import Ejercicio
from .apis.workout import get_rutine
from homepage.models import UsuarioApp
import pandas as pd
import random

#Funcion para conseguir la informacion de la api y generar la rutina de ejercicios
def rutina(request):

    seleccion = seleccion_intensidad(request)

    if request.method == 'POST':
        form = Makerutine(request.POST)
        if form.is_valid():
            intensidades = request.POST.getlist('intensidades[]')
            dias = request.POST.getlist('dias[]')
            musculos = request.POST.getlist('musculos[]')
            user = request.user

            for intensidad, dia, musculo in zip(intensidades, dias, musculos):
                rutina = get_rutine(musculo, intensidad)
                
                if rutina:
                    ejercicio_aleatorio = random.choice(rutina) #Se escoge un ejercicio aleatorio segun los parametros que ponga el usuario
                    historico_rutina = Ejercicio(
                        user=user,
                        intensity=ejercicio_aleatorio['intensity'],
                        muscles=ejercicio_aleatorio['muscles'],
                        day=dia,
                        sets=ejercicio_aleatorio['sets'],
                        reps_min=ejercicio_aleatorio['reps_min'],
                        reps_max=ejercicio_aleatorio['reps_max'],
                        workout=ejercicio_aleatorio['workout']
                    )
                    historico_rutina.save()

            return redirect('misrutinas')
    else:
            form = Makerutine()

    return render(request, 'home/generar_rutina.html', {
                'form': form,
                'intensidad_predeterminada': seleccion})



#Funcion para ver los ejercicios que el usurio ha creado
def ver_ejercicios(request):
    ejercicios = Ejercicio.objects.filter(user=request.user) #Llamada a la base de datos
    
    data = []
    for ejercicio in ejercicios:
        data.append({
            'id': ejercicio.id,
            'day': ejercicio.day,
            'muscles': ejercicio.muscles,
            'intensity': ejercicio.intensity,
            'sets': ejercicio.sets,
            'reps_min': ejercicio.reps_min,
            'reps_max': ejercicio.reps_max,
            'workout' : ejercicio.workout
        })
    df = pd.DataFrame(data)
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
    
    if not df.empty: #Si la base de datos no está vacia, clasificamos las rutinas segun el dia de la semana
        df['day'] = pd.Categorical(df['day'], categories=days_of_week, ordered=True)
        df = df.sort_values('day')

        ejercicios_por_dia = df.groupby('day', observed=False).apply(lambda x: x.to_dict(orient='records')).to_dict()
    else:
        ejercicios_por_dia = {}
    
    return render(request, 'home/mis_ejercicios.html', {'ejercicios_por_dia': ejercicios_por_dia})


#Funcion para editar los ejercicios que tiene el usuario en su rutina
def editar_rutina(request, ejercicio_id):
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)

    if request.method == 'POST':
        form = EditRutina(request.POST, instance=ejercicio)
        if form.is_valid():
            form.save()
            return redirect('misejercicios')
    else:
        form = EditRutina(instance=ejercicio)
    
    return render(request, 'home/edicion_rutinas.html', {'form': form, 'ejercicio': ejercicio})

#Funcion para eliminar un ejercicio que tiene el usuario en su rutina
def eliminar_rutina(request, ejercicio_id):
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)
    ejercicio.delete()
    return redirect('misejercicios')


#Funciones auxiliares

#Funcion para relacionar el nivel de actividad con la intensidad de un ejercicio
def seleccion_intensidad(request):
    intensidad_predeterminada = ''

    if request.user.is_authenticated:
        datos_usuario = UsuarioApp.objects.get(user=request.user)
        traduccion_actividad = {
            'sedentary': 'Sedentario',
            'light exercise': 'Bajo',
            'moderate exercise': 'Medio',
            'hard exercise': 'Alto',
            'professional athlete': 'Atleta profesional'
        }
        nivel_actividad = traduccion_actividad[datos_usuario.nivel_actividad]

        if nivel_actividad in ['Sedentario', 'Bajo']:
            intensidad_predeterminada = 'Beginner'
        elif nivel_actividad in ['Medio', 'Alto']:
            intensidad_predeterminada = 'Intermediate'
        elif nivel_actividad == 'Atleta profesional':
            intensidad_predeterminada = 'Expert'
        else:
            intensidad_predeterminada = ''
        
    return intensidad_predeterminada 