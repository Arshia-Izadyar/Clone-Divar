from django.urls import path
from .views import AdvertisementCityListView, AdvertisementDetailView


urlpatterns = [
    path("<slug:city>/", AdvertisementCityListView.as_view(), name="adv-list"),
    path("<int:pk>/detail/", AdvertisementDetailView.as_view(), name="adv-detail"),
    
]
