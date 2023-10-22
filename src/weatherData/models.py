from django.db import models


class WeatherData(models.Model):
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()  # Temperature in Celsius
    feels_like_temp = models.FloatField()  # Feels-like temperature in Celsius
    humidity = models.FloatField()  # Humidity in percentage
    wind_speed = models.FloatField()  # Wind speed in meters per second
    cloud_cover = models.FloatField()  # Cloud cover percentage
    visibility = models.FloatField()  # Visibility in meters
    weather_desc = models.CharField(max_length=255)
    icon = models.CharField(max_length=10,)
    forecast_data = models.JSONField(null=False, default=None)

    def __str__(self):
        return f"Weather data for {self.location} at {self.timestamp}"

    class Meta:
        db_table = "WeatherData"