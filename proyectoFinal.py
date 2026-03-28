import tkinter as tk
import requests 
import datetime

def obtener_temperatura(ciudad):
    API_KEY = "b659ac379534e31a9554ad46824f94d2"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

    respuesta = requests.get(URL)
    datos = respuesta.json()

    print(datos)

    if respuesta.status_code == 200: 
        temperatura_celsius = datos["main"]["temp"]
        temperatura_kelvin = temperatura_celsius + 273.15
        temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

        return temperatura_celsius, temperatura_kelvin, temperatura_fahrenheit
    else:
        return None

