from django.urls import path
from .views import AdvertisementCityListView


urlpatterns = [
    path("<slug:city>/", AdvertisementCityListView.as_view(), name="adv-list"),
]
