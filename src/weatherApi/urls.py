from django.urls import path
from weatherApi.scheduler import start_jobs
from weatherApi.views import FetchAndStoreWeatherData

urlpatterns = [
    path(
        "weather/<str:location>/",
        FetchAndStoreWeatherData.as_view(),
        name="weather-data",
    ),
]

# start_jobs()