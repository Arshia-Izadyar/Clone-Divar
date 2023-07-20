from django.urls import path
from .views import AdvertisementCityListView, AdvertisementDetailView, AdvertisementCityCategoryListView


urlpatterns = [
    path("<slug:city>/", AdvertisementCityListView.as_view(), name="adv-list"),
    path("<int:pk>/detail/", AdvertisementDetailView.as_view(), name="adv-detail"),
    path("<slug:city>/<slug:category>/", AdvertisementCityCategoryListView.as_view(), name="adv-category")
    
]
