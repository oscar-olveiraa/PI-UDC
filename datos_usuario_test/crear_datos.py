#!/bin/python3

from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

def calcular_tdee(peso):
    return (10*peso + 6.25*altura - 5*edad + 5)*1.2


fecha_inicio=datetime(2021, 1, 1).date()
peso_inicial=140
altura=180
edad=30
historial = [{
    "y":2021,
    "m": 1,
    "d": 2,
    "peso": 140.00,
    "tdee": calcular_tdee(peso_inicial),
    }]

for agno in range(36):
    fecha_inicio = fecha_inicio + relativedelta(months=1)
    if random.uniform(0, 1) >= 0.75:
        peso_inicial = peso_inicial * random.uniform(1.01, 1.03)
    else:
        peso_inicial = peso_inicial * random.uniform(0.97, 0.99)
    historial.append({
            "y": fecha_inicio.year,
            "m": fecha_inicio.month,
            "d": fecha_inicio.day,
            "peso": round(peso_inicial,2),
            "tdee": round(calcular_tdee(peso_inicial), 2)
        })

with open("datos_usuario.csv", "w") as datos:
    datos.write('year,month,day,peso,tdee\n')
    for i in historial:
        datos.write(f"{i['y']},{i['m']},{i['d']},{i['peso']},{i['tdee']}" + "\n")

