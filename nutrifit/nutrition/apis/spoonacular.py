import requests

_token = '9046fca1ebed412d9794e98d2d9d6cbf'

def get_recipe_list(name=None, type=None, diet=None, cuisine=None, intolerances=None, maxReadyTime=None, maxCalories=None,
                    minCalcium = None, minCopper = None, minFluoride = None, minIodine = None, minIron = None, minMagnesium = None,
                    minManganese = None, minPhosphorus = None, minSelenium = None, minZinc = None, minPotassium = None,
                    minSodium = None):
    """
    Args:
        name (str): Coincidencias con el nombre de la receta
        type (str): Tipo de comida (Principal, snack, bebida...).
        diet (str): Dieta alimenticia a la que se adapten las recetas.
        cuisine (str): Gastronomía según origen de la receta
        intolerances (str): Intolerancias alimenticias que excluyen recetas no compatibles
        maxReadyTime (int): Tiempo máximo que debería tardar en cocinarse la receta
        maxCalories (int): Maximo de calorías
        min'Nutriente' (int): Mínimo de miligramos que debe contener del micronutriente seleccionado según el histórico del usuario
    Return:
        Lista de recetas
    """

    url="https://api.spoonacular.com/recipes/complexSearch"  

    querystring = {
        "apiKey": _token,
    }

    if name:
        querystring["titleMatch"] = name
    if type:
        querystring["type"] = ",".join(type)
    if diet:
        querystring["diet"] = ",".join(diet)
    if cuisine:
        querystring["cuisine"] = ",".join(cuisine)
    if intolerances:
        querystring["intolerances"] = ",".join(intolerances)
    if maxReadyTime:
        querystring["maxReadyTime"] = maxReadyTime
    if maxCalories:
        querystring["maxCalories"] = maxCalories
    if minCalcium:
        querystring["minCalcium"] = minCalcium
    if minCopper:
        querystring["minCopper"] = minCopper
    if minFluoride:
        querystring["minFluoride"] = minFluoride
    if minIodine:
        querystring["minIodine"] = minIodine
    if minIron:
        querystring["minIron"] = minIron
    if minMagnesium:
        querystring["minMagnesium"] = minMagnesium
    if minManganese:
        querystring["minManganese"] = minManganese
    if minPhosphorus:
        querystring["minPhosphorus"] = minPhosphorus
    if minPotassium:
        querystring["minPotassium"] = minPotassium
    if minSelenium:
        querystring["minSelenium"] = minSelenium
    if minSodium:
        querystring["minSodium"] = minSodium

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    json_response = response.json()

    return json_response.get('results', [])

def get_recipe_details(id: int, includeNutrition: bool = True, addWinePairing: bool = False, addTasteOpen: bool = False):
    """
    Args:
        id (int): Número único que identifica una receta específica
        includeNutrition (bool): Incluye datos de nutrientes por ración
        addWinePairing (bool): Agrega un vino que vaya bien con la receta
        addTasteOpen (bool): Agrega datos del sabor de la receta
    Return:
        Informacion de la receta <id>
    """

    url = f"https://api.spoonacular.com/recipes/{id}/information"

    querystring = {
        "apiKey": _token,
        "includeNutrition": includeNutrition,
        "winePairing": addWinePairing,
        "taste": addTasteOpen,
    }

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    json_response = response.json()

    return json_response
