from django.test import TestCase, Client
from unittest.mock import patch, Mock
from .views import get_rutine
from django.contrib.auth.models import User
from exercices.models import Ejercicio
from homepage.models import UsuarioApp
from django.urls import reverse

#Test para la API
class GetRutineTestCase(TestCase):

    def setUP(self):
        pass

    @patch('requests.get') # Decorador para simular requests.get con un Mock
    def test_get_rutine(self, mock_get):
       
        mock_response_data = [
            {
                "Muscles": "Chest",
                "Intensity_Level": "Beginner",
                "WorkOut": "Bench Press",
                "Beginner Sets": "3 sets of 10-12 reps",
                "Intermediate Sets": "4 sets of 12-15 reps",
                "Expert Sets": "5 sets of 10-12 reps"
            }
        ]
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response_data

        result = get_rutine("Chest", "Beginner") # Chamada á funcion da API

        expected_result = [
            {
                "muscles": "Chest",
                "intensity": "Beginner",
                "workout": "Bench Press",
                "sets": 3,
                "reps_min": 10,
                "reps_max": 12
            }
        ]

        self.assertEqual(result, expected_result)


#Test para simular todas las acciones que haria un usuario en la creacion de una rutina
class RutinaTestCase(TestCase):
     def setUp(self):
        self.u = User.objects.create_user(username="testeo", password="testpassed")
        self.u.save()
        self.client = Client()
        ua = UsuarioApp(user=self.u, email="testeo@test.test", sexo="male",estatura=180, edad=30, peso_act=140, peso_des=90, nivel_actividad='sedentary').save()

        # Creamos un ejercicio de prueba
        self.ejercicio = Ejercicio.objects.create(
            user=self.u,
            intensity='Beginner',
            muscles='Biceps',
            day='Monday',
            sets=3,
            reps_min=8,
            reps_max=12,
            workout='Flexiones de bíceps'
        )

        # Inicializamos el cliente
        self.client = Client()

     def test_creacion_edicion_eliminacion_rutina(self):

        self.client.login(username='testuser', password='testpassword')

        # Generamos una nueva rutina
        response = self.client.post(reverse('misrutinas'), {
            'intensidad': 'Beginner',
            'dia': 'Monday',
            'musculo': 'Biceps'
        })

        # Verificamos que se haya creado correctamente
        self.assertEqual(response.status_code, 302)  

        nuevo_ejercicio_id = Ejercicio.objects.latest('id').id

        # Verificamos que el ejercicio se haya creado correctamente
        nuevo_ejercicio = Ejercicio.objects.get(id=nuevo_ejercicio_id)
        self.assertEqual(nuevo_ejercicio.user, self.u)
        self.assertEqual(nuevo_ejercicio.intensity, 'Beginner')
        self.assertEqual(nuevo_ejercicio.muscles, 'Biceps')
        self.assertEqual(nuevo_ejercicio.day, 'Monday')

        # Editamos el ejercicio recién creado
        response = self.client.post(reverse('editarutina', args=[nuevo_ejercicio_id]), {
            'sets': 4,
            'reps_min': 10,
            'reps_max': 15
        })

        # Verificamos que se haya editado correctamente
        ejercicio_editado = Ejercicio.objects.get(id=nuevo_ejercicio_id)
        self.assertEqual(ejercicio_editado.sets, 4)
        self.assertEqual(ejercicio_editado.reps_min, 10)
        self.assertEqual(ejercicio_editado.reps_max, 15)

        # Eliminamos el ejercicio
        response = self.client.post(reverse('eliminarutina', args=[nuevo_ejercicio_id]))

        # Verificamos que se haya eliminado correctamente
        with self.assertRaises(Ejercicio.DoesNotExist):
            Ejercicio.objects.get(id=nuevo_ejercicio_id)


