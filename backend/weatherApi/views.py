from django.shortcuts import render

# Create your views here.

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from weatherData.models import WeatherData
from .serializers import WeatherDataSerializer

from dotenv import load_dotenv

load_dotenv()
import os
api_key = os.getenv("API_KEY")
print('lalalalalalll ', api_key)
class FetchAndStoreWeatherData(APIView):
    def get(self, request, location):
        try:
            # Make a request to the OpenWeather API
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
            print(url)
            # https://api.openweathermap.org/data/2.5/weather?q=delhi&units=metric&appid=9f1ba70998f8f9c45e2df88ab5846c07
            response = requests.get(url)
            data = response.json()
            print(data)

            # Extract relevant data from the API response
            temperature = data['main']['temp']
            feels_like_temp = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            cloud_cover = data['clouds']['all']
            visibility = data.get('visibility', 0)  # visibility might not be present in the response

            # Create a new WeatherData object and save it to the database
            weather_data = WeatherData(
                location=location,
                temperature=temperature,
                feels_like_temp=feels_like_temp,
                humidity=humidity,
                wind_speed=wind_speed,
                cloud_cover=cloud_cover,
                visibility=visibility
            )
            weather_data.save()

            # Serialize and return the stored data
            serializer = WeatherDataSerializer(weather_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)