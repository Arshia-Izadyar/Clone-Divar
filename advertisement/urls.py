from django.urls import path, re_path
from .views import AdvertisementCityListView, AdvertisementDetailView, AdvertisementCityCategoryListView, AdvertisementPostView, AdvertisementUpdateView, AdvertisementDeleteView


urlpatterns = [
    path("list/<slug:city>/", AdvertisementCityListView.as_view(), name="adv-list"),
    path("<int:pk>/detail/", AdvertisementDetailView.as_view(), name="adv-detail"),
    path("list/<slug:city>/<slug:category>/", AdvertisementCityCategoryListView.as_view(), name="adv-category"),
    re_path(r"^add/$", AdvertisementPostView.as_view(), name="adv-add"),
    path("update/<int:pk>/", AdvertisementUpdateView.as_view(), name="adv-update"),
    path("delete/<int:pk>/", AdvertisementDeleteView.as_view(), name="adv-delete"),
    
    
]
