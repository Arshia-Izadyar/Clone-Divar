from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import Location

from django.http import HttpResponse

class LocationList(ListView):
    model = Location
    template_name = "location/location_list.html"
    context_object_name = "locations"
    queryset = Location.objects.all()

