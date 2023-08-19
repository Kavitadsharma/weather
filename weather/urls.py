from django.urls import path
from weather_data.views import get_weather, create_weather, update_weather, delete_weather

urlpatterns = [
    path('weather/<str:city>/', get_weather, name='weather'),
    path('weather/', create_weather, name='create_weather'),
    path('weather/<str:city>/', update_weather, name='update_weather'),
    path('weather/<str:city>/', delete_weather, name='delete_weather'),
]
