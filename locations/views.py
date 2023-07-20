from django.shortcuts import render
from django.views.generic import ListView

from .models import Location

class LocationList(ListView):
    model = Location
    template_name = "location/location_list.html"
    context_object_name = "locations"
    queryset = Location.objects.all()