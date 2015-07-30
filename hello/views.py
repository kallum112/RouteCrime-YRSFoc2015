from django.shortcuts import render
from django.http import HttpResponse
from postcodes import PostCoder
from police_api import PoliceAPI
import requests
from geolocation.google_maps import GoogleMaps
g_m = GoogleMaps(api_key='AIzaSyAGwOOqFQPqt6xyG3UPVkh9dXGeNN4_kpg')

from .models import Greeting

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    
    return HttpResponse('<h1>' + "Welcome To RouteCode Beta" + '</h1>' )
    return HttpResponse("<p> Enter Postcode </p>")
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

