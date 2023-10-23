from weatherData.models import WeatherData
import requests
from dotenv import load_dotenv
from weatherApi.views import get_forecast_data
load_dotenv()
import os

api_key = os.getenv("API_KEY")
base_url = "https://api.openweathermap.org/data/2.5"

def scheduled_update():
    try:

        location = "New Delhi"
        weather_data = WeatherData.objects.get(location=location)
        url = f"{base_url}/weather?q={location}&units=metric&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract relevant data from the API response
        temperature = data["main"]["temp"]
        feels_like_temp = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        cloud_cover = data["clouds"]["all"]
        visibility = data.get("visibility", 0)
        weather_desc = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
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
            forecast_data=forecast_data,
        )
        weather_data.save()

    except Exception as e:
        print(f"Erro {e}")
        

