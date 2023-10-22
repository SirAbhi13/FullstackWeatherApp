from django.shortcuts import render

# Create your views here.

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from weatherData.models import WeatherData
from .serializers import WeatherDataSerializer
import json
from datetime import datetime
import pytz

from dotenv import load_dotenv

load_dotenv()
import os
api_key = os.getenv("API_KEY")
base_url = "https://api.openweathermap.org/data/2.5"

class FetchAndStoreWeatherData(APIView):
    def get(self, request, location):
        try:
            # Make a request to the OpenWeather API
            url = f"{base_url}/weather?q={location}&units=metric&appid={api_key}"
            # https://api.openweathermap.org/data/2.5/weather?q=delhi&units=metric&appid=9f1ba70998f8f9c45e2df88ab5846c07
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Extract relevant data from the API response
            temperature = data['main']['temp']
            feels_like_temp = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            cloud_cover = data['clouds']['all']
            visibility = data.get('visibility', 0) 
            weather_desc = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            forecast_data = get_forecast_data(location)

            # Create a new WeatherData object and save it to the database
            weather_data = WeatherData(
                location=location,
                temperature=temperature,
                feels_like_temp=feels_like_temp,
                humidity=humidity,
                wind_speed=wind_speed,
                cloud_cover=cloud_cover,
                visibility=visibility,
                weather_desc=weather_desc,
                icon=icon,
                forecast_data=forecast_data
            )
            weather_data.save()

            # Serialize and return the stored data
            serializer = WeatherDataSerializer(weather_data)
            print (serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        


def get_forecast_data(location):

    # https://api.openweathermap.org/data/2.5/forecast?q=delhi&units=metric&appid=9f1ba70998f8f9c45e2df88ab5846c07
    try:
        endpoint = f"{base_url}/forecast?q={location}&units=metric&appid={api_key}"
        response = requests.get(endpoint)
        response.raise_for_status()
        data =  response.json()
        forecast_data = []
        
        for i,forecast in enumerate(data['list']):
            if i>5:
                break
            dt = forecast["dt"]
            temp = forecast['main']['temp']
            dt_txt = forecast["dt_txt"]

            item_data = {
            "dt": dt,
            "temp": temp,
            "dt_txt": dt_txt
            }            
            forecast_data.append(item_data)


        def convert_to_ist_and_format(timestamp):
            utc_time = datetime.utcfromtimestamp(timestamp)
            utc_time = pytz.utc.localize(utc_time)
            ist_timezone = pytz.timezone('Asia/Kolkata')
            ist_time = utc_time.astimezone(ist_timezone)
            formatted_time = ist_time.strftime("%I:%M %p")
            return formatted_time

        # Iterate through the data and update the 'temp' and 'dt_txt' fields
        for item in forecast_data:
            item['temp'] = round(item['temp'], 2)  # Round temperature to 2 decimal places
            item['dt_txt'] = convert_to_ist_and_format(item['dt'])
        
        return forecast_data

    except requests.exceptions.HTTPError as err:
        raise err
        