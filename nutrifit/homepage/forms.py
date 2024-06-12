from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from crispy_forms.layout import Submit, Layout, ButtonHolder
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ValidationError  
from homepage.models import UsuarioApp, Historico, Historico_micronutrientes
from homepage.apis.health import *
from threading import Thread
from django.utils import timezone


class UserRegisteredForms(UserCreationForm):
    SEX_CHOICES = (
        ('male', 'Masculino'),
        ('female', 'Femenino')
    )

    nivel_actividad_opciones = (
        ('sedentary', 'Sedentario'),
        ('light exercise', 'Bajo'),
        ('moderate exercise', 'Medio'),
        ('hard exercise', 'Alto'),
        ('professional athlete','Atleta profesional')
    )
    username = forms.CharField(label="Usuario", min_length=4, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', min_length=8,widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirma contraseña', min_length=8,widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'class': 'form-control'}),)
    email = forms.EmailField(label='Correo',widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    sexo = forms.ChoiceField(label='Sexo', choices=SEX_CHOICES, widget=forms.RadioSelect)
    estatura = forms.FloatField(label='Estatura(cm)', min_value=0, max_value=240,widget=forms.NumberInput(attrs={'placeholder': 'Estatura', 'style': 'width: 150px;','class': 'form-control'}))
    peso_deseado = forms.FloatField(label='Peso deseado(kg)', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Peso deseado', 'style': 'width: 150px;','class': 'form-control'}))
    peso_actual = forms.FloatField(label='Peso actual(kg)', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Peso actual', 'style': 'width: 150px;','class': 'form-control'}))
    edad = forms.IntegerField(label="Edad", min_value=0, widget=forms.NumberInput(attrs={'class':'form-control'}))
    nivel_actividad = forms.ChoiceField(label="Nivel de actividad fisico", choices=nivel_actividad_opciones, widget=forms.RadioSelect)
    

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'sexo', 'edad', 'estatura', 'peso_actual', 'peso_deseado', 'nivel_actividad']
        help_texts = {k:"" for k in fields}
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()  
        if UsuarioApp.objects.filter(email=email).exists():
            raise ValidationError('El email ya existe')
        return email
    
    def save(self, commit = True):  

        user = User.objects.create_user(  
            username=self.cleaned_data['username'],    
            password=self.cleaned_data['password1'],
            email = self.cleaned_data['email']
        )

        sexo_cleaned = self.cleaned_data['sexo']
        edad_cleaned = self.data['edad']
        estatura_cleaned = self.data['estatura']
        peso_act_cleaned = self.data['peso_actual']
        peso_des_cleaned = self.data['peso_deseado']
        nivel_actividad_cleaned = self.cleaned_data['nivel_actividad']

        uapp = UsuarioApp(user = user, email = self.cleaned_data['email'], sexo = sexo_cleaned, edad = int(edad_cleaned), estatura = int(estatura_cleaned), peso_act = float(peso_act_cleaned), peso_des = float(peso_des_cleaned), peso_origen=float(peso_act_cleaned), nivel_actividad = nivel_actividad_cleaned)
        uapp.save()

        #micronutrientes = get_micronutrients(sexo_cleaned[0], int(edad_cleaned[0]))
        t = Thread(target=self._save_micronutrients, args=[sexo_cleaned, int(edad_cleaned), user])
        t.setDaemon(True)
        t.start()

        historico = Historico(user = user, date=timezone.now(), tdee = get_tdee(int(estatura_cleaned), float(peso_act_cleaned), sexo_cleaned, int(edad_cleaned), nivel_actividad_cleaned), peso = float(peso_act_cleaned))
        #historico_mic = Historico_micronutrientes(user = user, calcium = micronutrientes['calcium'], chromium = micronutrientes['chromium'], copper = micronutrientes['copper'], fluoride = micronutrientes['fluoride'], iodine = micronutrientes['iodine'], iron = micronutrientes['iron'], magnesium = micronutrientes['magnesium'], manganese = micronutrientes['manganese'], molybdenum = micronutrientes['molybdenum'], phosphorus = micronutrientes['phosphorus'], selenium = micronutrientes['selenium'], zinc = micronutrientes['zinc'],potassium = micronutrientes['potassium'], sodium = micronutrientes['sodium'],chloride = micronutrientes['chloride'])

        historico.save()
        #historico_mic.save()

        return user
    
    def _save_micronutrients(self, sexo, edad, user):
        micronutrientes = get_micronutrients(sexo, edad)
        historico_mic = Historico_micronutrientes(user = user, calcium = micronutrientes['calcium'], chromium = micronutrientes['chromium'], copper = micronutrientes['copper'], fluoride = micronutrientes['fluoride'], iodine = micronutrientes['iodine'], iron = micronutrientes['iron'], magnesium = micronutrientes['magnesium'], manganese = micronutrientes['manganese'], molybdenum = micronutrientes['molybdenum'], phosphorus = micronutrientes['phosphorus'], selenium = micronutrientes['selenium'], zinc = micronutrientes['zinc'],potassium = micronutrientes['potassium'], sodium = micronutrientes['sodium'],chloride = micronutrientes['chloride'])
        historico_mic.save()
    
    def get_username(self):
        return self.cleaned_data['username']
    
    def get_passwd(self):
        return self.cleaned_data['password1']
        

class UserLoginForms(forms.Form):
    
    correo = forms.EmailField(label='Correo', widget=forms.EmailInput)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['correo', 'password']
        help_texts = {k:"" for k in fields}


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'type': 'hidden'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].widget.attrs['label'] = 'Nombre de usuario'

    
class ExtraProfileForm(forms.ModelForm):

    SEX_CHOICES = (
        ('male', 'Masculino'),
        ('female', 'Femenino')
    )

    nivel_actividad_opciones = (
        ('sedentary', 'Sedentario'),
        ('light exercise', 'Bajo'),
        ('moderate exercise', 'Medio'),
        ('hard exercise', 'Alto'),
        ('professional athlete','Atleta profesional')
    )

    email = forms.EmailField(label='Correo',widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    sexo = forms.ChoiceField(label='Sexo', choices=SEX_CHOICES, widget=forms.RadioSelect)
    estatura = forms.FloatField(label='Estatura(cm)', min_value=0, max_value=240,widget=forms.NumberInput(attrs={'placeholder': 'Estatura', 'style': 'width: 150px;','class': 'form-control'}))
    peso_des = forms.FloatField(label='Peso deseado(kg)', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Peso deseado', 'style': 'width: 150px;','class': 'form-control'}))
    peso_act = forms.FloatField(label='Peso actual(kg)', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Peso actual', 'style': 'width: 150px;','class': 'form-control'}))
    edad = forms.IntegerField(label="Edad", min_value=0, widget=forms.NumberInput(attrs={'class':'form-control'}))
    nivel_actividad = forms.ChoiceField(label="Nivel de actividad fisico", choices=nivel_actividad_opciones, widget=forms.RadioSelect)

    class Meta:
        model = UsuarioApp
        fields = ('email', 'sexo', 'estatura', 'edad', 'peso_act', 'peso_des', 'nivel_actividad')



class NuevoPeso(forms.ModelForm):
    peso_act = forms.FloatField(label="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Actualizar peso (kg)','style': 'width: 200px; margin: auto;','class': 'form-control'}))

    class Meta:
        model = UsuarioApp
        fields = ('peso_act', )

class RangoFecha(forms.Form):
     
    desde = forms.DateField(
        label = "Desde",
        #required = True,
        widget = forms.DateInput(format="$b %d, %Y", attrs={"type": "date", 'style': 'width: 175px; margin: auto;', 'class':'form-control col'}),
        input_formats=["$b %d, %Y"]
    )
       
    hasta = forms.DateField(
        label = "Hasta",
        #required = True,
        widget = forms.DateInput(format="$b %d, %Y", attrs={"type": "date", 'style': 'width: 175px; margin: auto;','class':'form-control col-auto'}),
        input_formats=["$b %d, %Y"]
    )

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', None)
        super(RangoFecha, self).__init__(*args, **kwargs)
        if initial:
            self.fields['desde'].widget.attrs['value'] = initial['desde']
            self.fields['hasta'].widget.attrs['value'] = initial['hasta']
    

    
    
    

    