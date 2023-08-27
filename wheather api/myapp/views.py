from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime
# Create your views here.

def index(request):
    # if there are no errors the code inside try will execute
    try:
    # checking if the method is POST
        if request.method == 'POST':
            API_KEY = '7187800dd3e300bf94c23539cf2bffd0'
            # getting the city name from the form input   
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY   
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
               
            response = requests.get(url).json()
            
            current_time = datetime.now()
             
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            
            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }

        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'home.html', context)
    
    except:
        return render(request, '404.html')