import requests

_token = '78084618a3mshe010eed7a8af134p136184jsn9abc16178f03'

def get_tdee(height: int, weight: float, gender: str,age: int, activity_level: str):
    """
    Args:
        height (int): Altura. Medida en centimetros.
        weight (float): Peso. Medido en kg.
        gender (str): Genero. Valores validos 'male' o 'female'
        age    (int): Años de edad.
        activity_level (str): Valores permitidos
            'sedentary'
            'light exercise'
            'moderate exercise'
            'hard exercise'
            'physical job'
            'professional athlete'
    Return:
        TDEE medido en kcal/day
    """

    url = "https://health-calculator-api.p.rapidapi.com/tdee"

    querystring = {
        "gender":gender,
        "age":age,
        "height":height,
        "weight":weight,
        "activity_level":activity_level,
        "equation":"mifflin"
        }
    headers = {
	"X-RapidAPI-Key": _token,
	"X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    json_response = response.json()

    return json_response['TDEE'].split()[0]

def get_micronutrients(gender: str, age: int):
    """
    Args:
        gender (str): Genero. Valores permitidos "male" o "female"
        age (int): Años de edad

    Returns:
        Diccionario de micronutrientes
    """

    url = "https://health-calculator-api.p.rapidapi.com/micronutrient"

    querystring = {
        "gender":gender,
        "age":age
    }

    headers = {
	    "X-RapidAPI-Key": _token,
	    "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
    }

    

    micronutrientes = ["calcium","chromium","copper","fluoride","iodine","iron","magnesium","manganese","molybdenum","phosphorus","selenium","zinc","potassium", "sodium", "chloride"]
    result = {}
    for micronutrient in micronutrientes:
        querystring["micronutrient"]=micronutrient

        response = requests.get(url, headers=headers, params=querystring)
        json_response = response.json()
    
        result[micronutrient] = float(json_response["Requirement"].split()[0])
    
    return result

