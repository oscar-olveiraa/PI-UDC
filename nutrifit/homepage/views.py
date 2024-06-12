from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisteredForms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import requests
from django.contrib import messages
from homepage.apis.health import *
from django.contrib.auth.models import User
from homepage.models import UsuarioApp, Historico, Historico_micronutrientes
from homepage.forms import EditProfileForm, ExtraProfileForm, NuevoPeso, RangoFecha
from django.contrib.auth.forms import PasswordChangeForm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone


def index(request):
    if request.user.is_authenticated:
        usuario = UsuarioApp.objects.get(user=request.user)
        form = NuevoPeso()        
        limites = obtener_limites_fecha(request)
        fechas = RangoFecha(initial={
                'desde': limites[0], 
                'hasta': limites[1]
                })
        
        # extension_temp es un discriminante en el nombre del archivo que permite
        # diferenciar el grafico por defecto de otro acotado por el usuario
        extension_temp = ""
        limite_inferior = None
        limite_superior = None

        if request.method == "POST":
            # Si el usuario modifica el rango de fechas
            if 'fechas' in request.POST:
                fechas = RangoFecha(initial={
                    'desde': request.POST['desde'],
                    'hasta': request.POST['hasta']
                })
                
                limite_inferior = datetime.strptime(request.POST['desde'], "%Y-%m-%d")
                limite_superior = datetime.strptime(request.POST['hasta'], "%Y-%m-%d")
                mostrar_grafica(request, 'tdee', limite_inferior, limite_superior)
                mostrar_grafica(request, 'peso', limite_inferior, limite_superior)
                extension_temp = "_temp"
            
            # Si el usuario introduce un nuevo peso
            if 'peso' in request.POST and form.is_valid:
                form = NuevoPeso(request.POST or None, instance=usuario)
                peso_act_cleaned = form.data['peso_act'],
                historico = Historico(user = request.user, date=timezone.now(), tdee = get_tdee(int(usuario.estatura), float(peso_act_cleaned[0]), usuario.sexo, int(usuario.edad), usuario.nivel_actividad), peso = float(peso_act_cleaned[0]))
                historico.save()
                form.save()
                mostrar_grafica(request, 'tdee')
                mostrar_grafica(request, 'peso')

        imc = round(obtener_imc(request),2)
        calorias = obtener_calorias(request)
        progreso = obtener_progreso(request)
        datos_peso = obtener_datos_peso(request, limite_inferior, limite_superior)
        datos_tdee = obtener_datos_tdee(request, limite_inferior, limite_superior)
        return render(request, 'home/home.html', {"datos_peso": datos_peso, "datos_tdee":datos_tdee,"progreso":progreso, "extension_temp":extension_temp,'pesoForm': form, "fechas": fechas, "imc": imc, "calorias": calorias})
    
    else:
        return render(request, 'home/home.html')


def login_user(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            
            email = request.POST['email']
            password = request.POST['password']
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "No se ha encontrado ningun usuario con esa combinación email/contraseña")
                return redirect('login')    
            

            if user is not None and user.check_password(raw_password=password):
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "No se ha encontrado ningun usuario con esa combinación email/contraseña")
                return redirect('login')    
            
        return render(request,'home/inicio_sesion.html', {})
    else:
        return redirect('home')
    
def perfil(request):
    if request.user.is_authenticated:
        datos_usuario = UsuarioApp.objects.get(user=request.user)
        traduccion_actividad={'sedentary': 'Sedentario',
        'light exercise': 'Bajo',
        'moderate exercise': 'Medio',
        'hard exercise': 'Alto',
        'professional athlete':'Atleta profesional'
        }
        datos_usuario.nivel_actividad = traduccion_actividad[datos_usuario.nivel_actividad]

        return render(request, 'home/perfil.html', {'datos_usuario':datos_usuario})
    else:
        return redirect('home')
    
def actualizar_perfil(request):
    traduccion_actividad={'sedentary': 'Sedentario',
        'light exercise': 'Bajo',
        'moderate exercise': 'Medio',
        'hard exercise': 'Alto',
        'professional athlete':'Atleta profesional'
        }
    
    if request.user.is_authenticated:
        # Se guardan los datos antiguos del usuario para comparar
        perfil  =UsuarioApp.objects.get(user=request.user)
        old_estatura = int(perfil.estatura)
        old_peso_act = float(perfil.peso_act)
        old_sexo = perfil.sexo
        old_edad = int(perfil.edad)
        old_nivel_actividad = perfil.nivel_actividad
        old_peso_des = perfil.peso_des

        user_form = EditProfileForm(request.POST or None, instance=request.user)
        profile_form = ExtraProfileForm(request.POST or None, instance=perfil)
        

        if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
            sexo_cleaned = profile_form.cleaned_data['sexo']
            edad_cleaned = profile_form.data['edad']
            estatura_cleaned = profile_form.data['estatura']
            peso_act_cleaned = profile_form.data['peso_act']
            peso_des_cleaned = profile_form.data['peso_des']
            nivel_actividad_cleaned = profile_form.cleaned_data['nivel_actividad']

            # Si se ha modificado el sexo o la edad, se recalculan los micronutrientes
            if old_sexo != sexo_cleaned or old_edad != int(edad_cleaned):
                micronutrientes = get_micronutrients(sexo_cleaned, int(edad_cleaned))
                historico_mic = Historico_micronutrientes(user = request.user, calcium = micronutrientes['calcium'], chromium = micronutrientes['chromium'], copper = micronutrientes['copper'], fluoride = micronutrientes['fluoride'], iodine = micronutrientes['iodine'], iron = micronutrientes['iron'], magnesium = micronutrientes['magnesium'], manganese = micronutrientes['manganese'], molybdenum = micronutrientes['molybdenum'], phosphorus = micronutrientes['phosphorus'], selenium = micronutrientes['selenium'], zinc = micronutrientes['zinc'],potassium = micronutrientes['potassium'], sodium = micronutrientes['sodium'],chloride = micronutrientes['chloride'])
                historico_mic.save()

            # Si se ha modificado la estatura, el peso, el sexo, la edad o el nivel de actividad
            # fisica se actualizan los historicos
            if old_estatura != int(estatura_cleaned) or old_peso_act != float(peso_act_cleaned) or old_sexo != sexo_cleaned or old_edad != int(edad_cleaned) or old_nivel_actividad != nivel_actividad_cleaned:
                historico = Historico(user = request.user, date=timezone.now(),tdee = get_tdee(int(estatura_cleaned), float(peso_act_cleaned), sexo_cleaned, int(edad_cleaned), nivel_actividad_cleaned), peso = float(peso_act_cleaned))
                historico.save()

            user_form.save()
            profile_form.save()
            
            if old_peso_des != peso_des_cleaned:
                usuarioapp = UsuarioApp.objects.get(user=request.user)
                usuarioapp.peso_origen = float(peso_act_cleaned)
                usuarioapp.save()

            mostrar_grafica(request, 'tdee')
            mostrar_grafica(request, 'peso')
            return redirect('perfil')
        
        else:
            return render(request, "home/editar_perfil.html", {'user_form': user_form, 'profile_form': profile_form})
    else:
        return redirect('home')
   

def register(request):
    if request.method == 'POST':
        form = UserRegisteredForms(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario creado con exito")
            mostrar_grafica(request, 'tdee')
            mostrar_grafica(request, 'peso')
            return redirect('home')

    else:
        form = UserRegisteredForms()
    context = {'form' : form}

    
    return render(request,'home/registro.html', context)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Ha cerrado sesión correctamente")
    return redirect('home')

def cambiar_contrasenha(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(data=request.POST, user=request.user)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Se ha actualizado la contraseña correctamente")
            return render(request, 'home/home.html', {})
            
                
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request, 'home/cambiar_contrasenha.html', {"form": form})
    else:
        return redirect('home')


def createuser(request):
    # Función que crea el usuario con datos precargados
    username = 'testing'
    password = '1234'
    email = 'test@nutrifit.com'
    fecha_creacion = datetime(2021, 2, 2)

    if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        
        # Lee los datos precargados, que están en formato csv
        df = pd.read_csv('/workspace/datos_usuario_test/datos_usuario.csv')
        peso_actual = 0

        for fila in df.iterrows():
            agno = int(fila[1]['year'])
            mes = int(fila[1]['month'])
            dia = int(fila[1]['day'])
            peso = fila[1]['peso']
            peso_actual = peso
            tdee = fila[1]['tdee']
            historico = Historico(user=user, date=datetime(agno, mes, dia), peso=peso, tdee=tdee)
            historico.save()


        userapp = UsuarioApp(user=user, email=email, sexo='male', estatura=180, edad=30, peso_act=peso_actual, peso_origen=140.0, peso_des=90, nivel_actividad='sedentary')
        userapp.save()

        historico_m = Historico_micronutrientes(user = user, date=fecha_creacion ,calcium = 1000.0, chromium = 35.0, copper = 900.0, fluoride = 4.0, iodine = 150.0, iron = 8.0, magnesium = 400.0, manganese = 2.3, molybdenum = 45.0, phosphorus = 700.0, selenium = 55.0, zinc = 11.0,potassium = 3400.0, sodium = 1500.0,chloride = 2300.0)
        historico_m.save()
        mostrar_grafica(request, 'tdee')
        mostrar_grafica(request, 'peso')

    return redirect('home')



def mostrar_grafica(request, tipo_grafico, limite_inferior_opcional=None, limite_superior_opcional=None):
    if tipo_grafico == 'tdee':
        # Se obitenen la columna tdee y date del historico del usuario entre los limites
        # especificados, en caso de que los haya
        historial_usuario = Historico.objects.filter(user=request.user, date__range=(limite_inferior_opcional or datetime.min, limite_superior_opcional or datetime.max)).values('date', 'tdee')
        

        titulo = 'Calorías diarias quemadas'
        etiqueta_y = 'TDEE'

    elif tipo_grafico == 'peso':
        # Se obitenen la columna peso y date del historico del usuario entre los limites
        # especificados, en caso de que los haya
        historial_usuario = Historico.objects.filter(user=request.user, date__range=(limite_inferior_opcional or datetime.min, limite_superior_opcional or datetime.max)).values('date', 'peso')
        titulo = 'Peso corporal'
        etiqueta_y = 'Peso(kg)'

    # Si hay resultados entre los limites especificados (en caso de que no haya
    # limites, este condicional devolvera siempre verdadero)
    if len(historial_usuario) > 0:
        df = pd.DataFrame(historial_usuario)
        df.plot(x='date', marker='o', linestyle='-', color='#8a2ce2') # antiguo color #00FF00

        # Limites del grafica
        if limite_inferior_opcional or limite_superior_opcional:
            if limite_inferior_opcional == datetime.min:
                limite_inferior = limite_inferior_opcional.date()    
            else:
                limite_inferior = limite_inferior_opcional.date() - relativedelta(months=1)
            
            if limite_superior_opcional == datetime.max:
                limite_superior = limite_superior_opcional.date()
            else:
                limite_superior = limite_superior_opcional.date() + relativedelta(months=1)
        else:
            limite_inferior = df['date'].min() - relativedelta(months=1)
            limite_superior = df['date'].max() + relativedelta(months=1)

        # Se convierten los limites de datetime.date a datetime
        limite_inferior = datetime.combine(limite_inferior, datetime.min.time())
        limite_superior = datetime.combine(limite_superior, datetime.min.time())
    
        plt.xlim(limite_inferior, limite_superior)
        plt.xlabel('Fecha', fontsize=16, fontweight='bold')
    else:
        plt.figure(figsize=(8,6))
        plt.xlabel('No se han encontrado valores para este intervalo', fontsize=16, fontweight='bold')
        


    plt.ylabel(etiqueta_y, fontsize=16, fontweight='bold')
    plt.title(titulo, fontsize=20, fontweight='bold')
    plt.grid(True, linewidth=1.5)
    plt.gca().set_facecolor('white')
    plt.gca().set_alpha(0.3)
    plt.xticks(rotation=45)


    plt.tight_layout()

    if limite_inferior_opcional or limite_superior_opcional:
        nombre_archivo = f'/workspace/nutrifit/homepage/static/grafica_{tipo_grafico}_{request.user.username}_temp.png'
    else:
        nombre_archivo = f'/workspace/nutrifit/homepage/static/grafica_{tipo_grafico}_{request.user.username}.png'
    plt.savefig(nombre_archivo)


# Funciones auxiliares
def obtener_limites_fecha(request):
    fechas = [registro.date for registro in Historico.objects.filter(user=request.user)]

    # Devuelve un tupla tal que (limite_inferior, limite_superior)
    s = pd.Series(fechas)
    return (s.min(), s.max())

def obtener_imc(request):
    user = UsuarioApp.objects.get(user=request.user)

    return user.peso_act / ((user.estatura / 100)**2)

    
def obtener_calorias(request):
    historico = Historico.objects.filter(user=request.user)
    
    return historico.last().tdee

def obtener_progreso(request):
    peso_act = request.user.usuarioapp.peso_act
    peso_des = request.user.usuarioapp.peso_des
    peso_origen = request.user.usuarioapp.peso_origen


    progreso = int((1 - ((peso_des - peso_act) / (peso_des - peso_origen))) * 100)
    
    if progreso < 0:
        progreso = 0
    elif progreso > 100:
        progreso = 100

    return progreso

def obtener_datos_peso(request, limite_inferior=None, limite_superior=None):
    historial_peso = Historico.objects.filter(user=request.user, date__range=(limite_inferior or datetime.min, limite_superior or datetime.max)).values('peso')
    
    if len(historial_peso) == 0:
        resultado = {
        "Maximo": 0,
        "Minimo": 0,
        "Media": 0,
        "Mediana": 0
    }
    else:
        df = pd.DataFrame(historial_peso)
        resultado = {
            "Maximo": round(df['peso'].max(), 2),
            "Minimo": round(df['peso'].min(), 2),
            "Media": round(df['peso'].mean(), 2),
            "Mediana": round(df['peso'].median(), 2)
        }

    return resultado

def obtener_datos_tdee(request, limite_inferior=None, limite_superior=None):
    historial_tdee = Historico.objects.filter(user=request.user, date__range=(limite_inferior or datetime.min, limite_superior or datetime.max)).values('tdee')
    
    if len(historial_tdee) == 0:
        resultado = {
        "Maximo": 0,
        "Minimo": 0,
        "Media": 0,
        "Mediana": 0
    }
    else:
        df = pd.DataFrame(historial_tdee)
        resultado = {
            "Maximo": round(df['tdee'].max(), 2),
            "Minimo": round(df['tdee'].min(), 2),
            "Media": round(df['tdee'].mean(), 2),
            "Mediana": round(df['tdee'].median(), 2)
        }

    return resultado





    
  