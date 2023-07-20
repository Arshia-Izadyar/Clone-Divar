from django.urls import path

from .views import UserProfile


urlpatterns = [
    path("", UserProfile.as_view(), name="profile"),
]
