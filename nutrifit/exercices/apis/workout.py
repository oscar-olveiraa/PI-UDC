import re
import requests

_token = '6988ec4449msh2fddc6757d3b3cbp135d12jsnef3d9fde58b8'

def get_rutine(muscles: str, intensity: str):
    url = "https://work-out-api1.p.rapidapi.com/search"
    querystring = {
        "Muscles": muscles,
        "Intensity_Level": intensity
    }
    headers = {
	    "x-rapidapi-key": _token,
	    "x-rapidapi-host": "work-out-api1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_response = response.json()

    
    filtered_results = []

    for exercise in json_response:
        if exercise.get('Muscles').lower() == muscles.lower() and exercise.get('Intensity_Level').lower() == intensity.lower(): #Dependiendo de la intensidad que indique el usuario, miramos el numero de series y repeticiones que tiene que hacer
            sets_reps = exercise.get(f'{intensity.capitalize()} Sets')
            sets_reps_numbers = list(map(int, re.findall(r'\d+', sets_reps))) #Buscamos solamente los numeros que del valor del campo escogido en la linea anterior y los guardamos en una lista
            
            if len(sets_reps_numbers) >= 3:
                exercise_info = {
                    "muscles": exercise.get('Muscles'),
                    "intensity": exercise.get('Intensity_Level'),
                    "workout": exercise.get('WorkOut'),
                    "sets": sets_reps_numbers[0],     #Accedemos a la posicion 1 de la lista (numero de series)
                    "reps_min": sets_reps_numbers[1], #Accedemos a la posicion 2 de la lista (numero de repeticiones mimimas)
                    "reps_max": sets_reps_numbers[2]  #Accedemos a la posicion 3 de la lista (numero de repeticiones maximas)
                }
                filtered_results.append(exercise_info)

    return filtered_results