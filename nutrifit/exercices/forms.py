from django import forms
from exercices.apis.workout import get_rutine
from exercices.models import Ejercicio

class Makerutine(forms.Form):
    options_intensity = [
        ('Beginner', 'principiante'),
        ('Intermediate', 'intermedio'),
        ('Expert', 'experto')
    ]

    options_day = [
        ('Monday', 'Lunes'),
        ('Tuesday', 'Martes'),
        ('Wednesday', 'Miercoles'),
        ('Thrusday', 'Jueves'),
        ('Friday', 'Viernes'),
        ('Saturday', 'Sabado'),
        ('Sunday', 'Domingo'),
    ]

    options_muscles = [
        ('Biceps','Biceps'),
        ('Triceps','Triceps'),
        ('Chest','Pecho'),
        ('Back','Espalda'),
        ('Legs','Piernas'),
        ('Abs','Abdominales'),
        ('Stretching','Estiramiento'),
        ('Warm Up','Calentamiento'),
        ('Lats','Dorsales'),
        ('Hamstring','Isquiotibiales'),
        ('Calves','Gemelos'),
        ('Quadriceps','Cuadriceps'),
        ('Trapezius','Trapecios'),
        ('Shoulders','Hombros'),
        ('Glutes','Gluteos'),
    ]
    
    intensidad = forms.ChoiceField(
        choices=options_intensity,
        label="Intensidad",
    )

    dia = forms.ChoiceField(
        choices=options_day,
        label="Día de la semana",
    )

    musculo = forms.ChoiceField(
        choices=options_muscles,
        label="Músculo"
    )


class EditRutina(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = ['day', 'sets', 'reps_min', 'reps_max']

    options_intensity = [
        ('Beginner', 'principiante'),
        ('Intermediate', 'intermedio'),
        ('Expert', 'experto')
    ]

    options_day = [
        ('Monday', 'Lunes'),
        ('Tuesday', 'Martes'),
        ('Wednesday', 'Miercoles'),
        ('Thrusday', 'Jueves'),
        ('Friday', 'Viernes'),
        ('Saturday', 'Sabado'),
        ('Sunday', 'Domingo'),
    ]

    options_muscles = [
        ('Biceps','Biceps'),
        ('Triceps','Triceps'),
        ('Chest','Pecho'),
        ('Back','Espalda'),
        ('Legs','Piernas'),
        ('Abs','Abdominales'),
        ('Stretching','Estiramiento'),
        ('Warm Up','Calentamiento'),
        ('Lats','Dorsales'),
        ('Hamstring','Isquiotibiales'),
        ('Calves','Gemelos'),
        ('Quadriceps','Cuadriceps'),
        ('Trapezius','Trapecios'),
        ('Shoulders','Hombros'),
        ('Glutes','Gluteos'),
    ]
    
    #intensity = forms.ChoiceField(choices=options_intensity, label="Intensidad", required=False)
    day = forms.ChoiceField(choices=options_day, label="Día de la semana", required=False)
    #muscles = forms.ChoiceField(choices=options_muscles, label="Músculo", required=False)
    sets = forms.IntegerField(min_value=0, max_value=1000, label="Series", required=False)
    reps_min = forms.IntegerField(min_value=0, max_value=1000, label="Repeticiones mínimas", required=False)
    reps_max = forms.IntegerField(min_value=0, max_value=1000, label="Repeticiones máximas", required=False)