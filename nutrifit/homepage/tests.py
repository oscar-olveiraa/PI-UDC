from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import UserRegisteredForms
from homepage.models import UsuarioApp, Historico, Historico_micronutrientes
from django.utils import timezone
from homepage.apis.health import *


class UserRegistrationTest(TestCase): 
    
    def setUp(self):
        u = User.objects.create_user(username="testeo", password="testpassed")
        u.save()
        ua = UsuarioApp(user=u, email="testeo@test.test", sexo="male",estatura=180, edad=30, peso_act=140, peso_des=90, nivel_actividad='sedentary').save()

        Historico(user=u, date=timezone.now(), tdee=2856, peso=140).save()
        Historico(user=u, date=timezone.now(), tdee=2821.19, peso=137.1).save()
        Historico(user=u, date=timezone.now(), tdee=2796.45, peso=135.04).save()

        Historico_micronutrientes(user=u, calcium=1000.0, chromium=35.0, copper=900.0, fluoride=4.0, iodine=150.0, iron=8.0, magnesium=400.0, manganese=2.3, molybdenum=45.0, phosphorus=700.0, selenium=55.0, zinc=11.0, potassium=3400.0, sodium=1500.0, chloride=2300.0).save()




    def test_loginSuccessful(self):
        username = "testeo"
        password = "testpassed"
        user = authenticate(username=username,password=password)
        self.assertIsNotNone(user)    
    
    def test_loginUnsuccessful(self):
        username = "paco@gmail.com"
        password = "cxt15aao"
        user = authenticate(username=username,password=password)
        self.assertIsNone(user)
    
    def test_Userapp(self):
        user = authenticate(username="testeo",password="testpassed")
        userapp = UsuarioApp.objects.get(user=user)
        
        self.assertEqual(userapp.email, 'testeo@test.test')
        self.assertEqual(userapp.sexo, 'male')
        self.assertEqual(userapp.estatura, 180)
        self.assertEqual(userapp.edad, 30)
        self.assertEqual(userapp.peso_act, 140)
        self.assertEqual(userapp.peso_des, 90)
        self.assertEqual(userapp.nivel_actividad, 'sedentary')

    def test_Historial(self):
        user = authenticate(username="testeo",password="testpassed")
        historial = Historico.objects.filter(user=user)
        primer_registro = historial.first()

        self.assertEqual(historial.count(), 3)
        self.assertEqual(primer_registro.peso, 140)
        self.assertEqual(primer_registro.tdee, 2856)

    def test_Historial_micronutrientes(self):
        user = authenticate(username="testeo",password="testpassed")
        historico = Historico_micronutrientes.objects.filter(user=user)
        primer_registro = historico.first()

        self.assertEqual(historico.count(), 1)
        self.assertEqual(primer_registro.calcium, 1000)
        self.assertEqual(primer_registro.chromium, 35)
        self.assertEqual(primer_registro.chloride, 2300)

# Test de la api
class ApiTest(TestCase):
    def setUP(self):
        pass

    def test_tdee(self):
        tdee = get_tdee(180, 140, 'male', 20, 'sedentary')

        self.assertEqual(tdee, '2916.0')

    def test_micronutrientes(self):
        micronutrientes = get_micronutrients('male', 20)

        self.assertEqual(micronutrientes['calcium'], 1000)
        self.assertEqual(micronutrientes['chromium'], 35)
        self.assertEqual(micronutrientes['chloride'], 2300)