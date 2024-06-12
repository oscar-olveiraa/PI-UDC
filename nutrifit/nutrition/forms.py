from django import forms

class RecipeSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=100, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por nombre', 'class': 'form-control'})
    )

    TIPO_PLATO = [
        ('main course', 'Plato principal'),
        ('side dish', 'Guarnición'),
        ('appetizer', 'Aperitivo'),
        ('dessert', 'Postre'),
        ('breakfast', 'Desayuno'),
        ('snack', 'Snack'),
        ('drink', 'Bebida'),
        ('soup', 'Sopa'),
        ('salad', 'Ensalada'),
        ('bread', 'Pan'),
        ('fingerfood', 'Fingerfood'),
        ('sauce', 'Salsa'),
    ]
    tipo_plato = forms.MultipleChoiceField(
        choices=TIPO_PLATO,
        widget=forms.CheckboxSelectMultiple,
        label='Tipo de plato',
        required=False
    )

    DIETA_CHOICES = [
        ('gluten_free', 'Gluten Free'),
        ('ketogenic', 'Ketogénica'),
        ('vegetarian', 'Vegetariana'),
        ('lacto_vegetarian', 'Lacto-Vegetariana'),
        ('ovo_vegetarian', 'Ovo-Vegetariana'),
        ('vegan', 'Vegana'),
        ('pescetarian', 'Pescetariana'),
        ('paleo', 'Paleolítica'),
        ('primal', 'Primal'),
        ('low_fodmap', 'Low FODMAP'),
        ('whole30', 'Whole30'),
    ]
    tipo_dieta = forms.MultipleChoiceField(
        choices=DIETA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Tipo de dieta',
        required=False
    )

    COCINA_CHOICES = [
        ('African', 'Africana'),
        ('Asian', 'Asiática'),
        ('American', 'Americana'),
        ('British', 'Inglesa'),
        ('Cajun', 'Cajun'),
        ('Caribbean', 'Caribeña'),
        ('Eastern European', 'Este-Europea'),
        ('European', 'Europea'),
        ('Chinese', 'China'),
        ('French', 'Francesa'),
        ('German', 'Alemana'),
        ('Greek', 'Griega'),
        ('Indian', 'India'),
        ('Irish', 'Irlandesa'),
        ('Italian', 'Italiana'),
        ('Japanese', 'Japonesa'),
        ('Jewish', 'Judía'),
        ('Korean', 'Coreana'),
        ('Latin American', 'Latinoamericana'),
        ('Mediterranean', 'Mediterránea'),
        ('Middle Eastern', 'Arábiga'),
        ('Nordic', 'Nórdica'),
        ('Spanish', 'Española'),
        ('Thai', 'Tailandesa'),
        ('Vietnamese', 'Vietnamita'),
    ]
    cocina = forms.MultipleChoiceField(
        choices=COCINA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Cocina',
        required=False
    )

    INTOLERANCIAS_CHOICES = [
        ('Dairy', 'Lácteos'),
        ('Egg', 'Huevo'),
        ('Gluten', 'Gluten'),
        ('Grain', 'Cereales'),
        ('Peanut', 'Cacahuete'),
        ('Seafood', 'Mariscos'),
        ('Sesame', 'Sésamo'),
        ('Shellfish', 'Crustáceos'),
        ('Soy', 'Soja'),
        ('Sulfite', 'Sulfitos'),
        ('Tree Nut', 'Frutos secos'),
        ('Wheat', 'Trigo'),
    ]
    intolerancias = forms.MultipleChoiceField(
        choices=INTOLERANCIAS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Intolerancias',
        required=False
    )

    TIEMPO_CHOICES = [
        ('menos15', '15'),
        ('menos45', '45'),
        ('mas45', '>45'),
    ]
    tiempo_preparacion = forms.ChoiceField(
        choices=TIEMPO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=False
    )

    CALORIAS_CHOICES = [
        ('max500', '500'),
        ('max1000', '1000'),
        ('max1500', '1500'),
        ('maxInf', '>1500')
    ]
    calorias = forms.ChoiceField(
        choices=CALORIAS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=False
    )

    NUTRIENTES_CHOICES = [
        ('minCalcium', 'Calcio'),
        ('minCopper', 'Cobre'),
        ('minFluoride', 'Fluor'),
        ('minIodine', 'Yodo'),
        ('minIron', 'Hierro'),
        ('minMagnesium', 'Magnesio'),
        ('minManganese', 'Manganeso'),
        ('minPhosphorus', 'Fosforo'),
        ('minSelenium', 'Selenio'),
        ('minZinc', 'Zinc'),
        ('minPotassium', 'Potasio'),
        ('minSodium', 'Sodio')
    ]
    nutrientes = forms.ChoiceField(
        choices=NUTRIENTES_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

