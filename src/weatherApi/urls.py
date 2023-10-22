from django.urls import path

from weatherApi.views import FetchAndStoreWeatherData

urlpatterns = [
    path(
        "weather/<str:location>/",
        FetchAndStoreWeatherData.as_view(),
        name="weather-data",
    ),
]
