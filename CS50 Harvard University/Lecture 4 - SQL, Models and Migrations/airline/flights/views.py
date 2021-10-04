from django.shortcuts import render
from django.http import HttpResponse
from . models import Flight, Passenger

# Create your views here.


def index(request):
    template = "flights/index.html"
    context = {"flights": Flight.objects.all()}
    return render(request, template, context)


def flight(request, flight_id):
    template = "flights/flight_detail.html"
    context = {"the_flight": Flight.objects.get(
        pk=flight_id), "passengers": Passenger.objects.all()}
    return render(request, template, context)
