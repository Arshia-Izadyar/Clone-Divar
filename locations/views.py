from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import Location

class LocationList(ListView):
    model = Location
    template_name = "location/location_list.html"
    context_object_name = "locations"
    queryset = Location.objects.all()
    
    
    def get(self, request, *args, **kwargs):
        city = self.request.GET.get('city')
        if city:
            # Set the city in a cookie with a one-week expiration time
            response = HttpResponseRedirect('/adv/')  # Redirect to the advertisements page
            response.set_cookie('selected_city', city, max_age=604800)  # One week in seconds
            return response
        return super().get(request, *args, **kwargs)