from django.urls import path
from .views import LocationListView, LocationNearestView, LocationCitiesView

urlpatterns = [
    path("", LocationListView.as_view(), name="location-list"),
    path("nearest/", LocationNearestView.as_view(), name="location-nearest"),
    path("cities/", LocationCitiesView.as_view(), name="location-cities"),
]