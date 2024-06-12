from django.shortcuts import render, redirect
from .forms import RecipeSearchForm
from nutrition.apis.spoonacular import *
import pandas as pd
import matplotlib.pyplot as plt
import os
from django.http import JsonResponse
from homepage.models import Historico_micronutrientes


def search_recipes(request):
    form = RecipeSearchForm(request.GET or None)
    recipes = None
    user = request.user
    historico = Historico_micronutrientes.objects.filter(user=user).last()
                

    if request.method == "GET" and request.GET:
        
        if form.is_valid():
            cleaned_data = form.cleaned_data

            nombre = cleaned_data.get('nombre')
            tipo_plato = cleaned_data.get('tipo_plato')
            tipo_dieta = cleaned_data.get('tipo_dieta')
            cocina = cleaned_data.get('cocina')
            intolerancias = cleaned_data.get('intolerancias')
            tiempo_preparacion = cleaned_data.get('tiempo_preparacion')
            calorias = cleaned_data.get('calorias')
            nutrientes = cleaned_data.get('nutrientes')

            if tiempo_preparacion == 'menos15':
                maxReadyTime = 15
            elif tiempo_preparacion == 'menos45':
                maxReadyTime = 45
            else:
                maxReadyTime = None

            if calorias == 'max500':
                maxCalorias = 500
            elif calorias == 'max1000':
                maxCalorias = 1000
            elif calorias == 'max1500':
                maxCalorias = 1500
            else:
                maxCalorias = None

            minCalcium = None
            minCopper = None
            minFluoride = None
            minIodine = None
            minIron = None
            minMagnesium = None
            minManganese = None
            minPhosphorus = None
            minSelenium = None
            minZinc = None
            minSodium = None
            minPotassium = None

            if nutrientes == "minCalcium":
                minCalcium = historico.calcium
            if nutrientes == "minCopper":
                minCopper = historico.copper
            if nutrientes == "minFluoride":
                minFluoride = historico.fluoride
            if nutrientes == "minIodine":
                minIodine = historico.iodine
            if nutrientes == "minIron":
                minIron = historico.iron
            if nutrientes == "minMagnesium":
                minMagnesium = historico.magnesium
            if nutrientes == "minManganese":
                minManganese = historico.manganese
            if nutrientes == "minPhosphorus":
                minPhosphorus = historico.phosphorus
            if nutrientes == "minSelenium":
                minSelenium = historico.selenium
            if nutrientes == "minZinc":
                minZinc = historico.zinc
            if nutrientes == "minSodium":
                minSodium = historico.sodium
            if nutrientes == "minPotassium":
                minPotassium = historico.potassium

            recipes = get_recipe_list(
                name=nombre, 
                type=tipo_plato, 
                diet=tipo_dieta, 
                cuisine=cocina, 
                intolerances=intolerancias, 
                maxReadyTime=maxReadyTime, 
                maxCalories=maxCalorias,
                minCalcium=minCalcium,
                minCopper=minCopper,
                minFluoride=minFluoride,
                minIodine=minIodine,
                minIron=minIron,
                minMagnesium=minMagnesium,
                minManganese=minManganese,
                minPhosphorus=minPhosphorus,
                minSelenium=minSelenium,
                minZinc=minZinc,
                minPotassium=minPotassium,
                minSodium=minSodium
            )

            # Debugging
            print(recipes)
            print(minCalcium)
            print(minCopper)
            
        else:
            print(form.errors)     

    return render(request, 'search_recipes.html', {'form': form, 'recipes': recipes, 'query_params': request.GET.urlencode()})


def convert_to_mg(amount, unit):
    conversion_factors = {
        'kcal': 1,
        'g': 1000,
        'mg': 1,
        'µg': 0.001,
        'IU': 0.0003
    }
    return amount * conversion_factors.get(unit, 1)

def recipe_details(request, recipe_id):
    recipe = get_recipe_details(recipe_id)

    nutrients = recipe['nutrition']['nutrients']
    df = pd.DataFrame(nutrients)

    df['amount_mg'] = df.apply(lambda row: convert_to_mg(row['amount'], row['unit']), axis=1)

    df = df[~df['name'].isin(['Calories', 'Carbohydrates'])]

    top5 = df.nlargest(5, 'amount_mg')
    others = df[~df.index.isin(top5.index)]
    
    others_sum = others['amount_mg'].sum()
    others_row = pd.DataFrame([{'name': 'Others', 'amount_mg': others_sum}])
    top5 = pd.concat([top5, others_row], ignore_index=True)
    top5.set_index('name', inplace=True)
    
    top5['amount_mg'].plot(kind='pie', labels=top5.index, autopct='%1.1f%%')

    nombre_archivo = f'/workspace/nutrifit/homepage/static/grafica_nutrientes_{recipe_id}.png'
    
    plt.ylabel('Cantidad en miligramos', fontsize=12, fontweight='bold')
    plt.savefig(nombre_archivo, transparent=True)

    plt.close()

    return render(request, 'details_recipe.html', {'recipe': recipe})

def delete_grafica(request, recipe_id):
    if request.method == 'DELETE':
        nombre_archivo = f'/workspace/nutrifit/homepage/static/grafica_nutrientes_{recipe_id}.png'
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)
            return JsonResponse({'status': 'success', 'message': 'File deleted'})
        else:
            return JsonResponse({'status': 'error', 'message': 'File not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})