from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.http import require_http_methods
import json

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@require_http_methods(["GET"])
def get_weather(request, city):
    try:
        data = weather_data[city]
        return JsonResponse(data)
    except KeyError:
        raise Http404("City not found")

@require_http_methods(["POST"])
def create_weather(request):
    try:
        body = json.loads(request.body)
        city = body['city']
        weather = body['weather']
        temperature = body['temperature']
        weather_data[city] = {'temperature': temperature, 'weather': weather}
        return HttpResponse(status=201)
    except json.JSONDecodeError:
        return HttpResponse(status=400)

@require_http_methods(["PUT"])
def update_weather(request, city):
    try:
        data = json.loads(request.body)
        if city in weather_data:
            weather_data[city].update(data)
            return HttpResponse(status=204)
        else:
            raise Http404("City not found")
    except json.JSONDecodeError:
        return HttpResponse(status=400)

@require_http_methods(["DELETE"])
def delete_weather(request, city):
    try:
        del weather_data[city]
        return HttpResponse(status=204)
    except KeyError:
        raise Http404("City not found")
