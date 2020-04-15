from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

def temphum(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'humidity', 'value': value}
            response = requests.post('http://127.0.0.1:8000/temphum/', args)
            # Convierte la respuesta en JSON
            temphum_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/temphum/')
    # Convierte la respuesta en JSON
    temphum = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temphum/temphum.html", {'temphum': temphum})
