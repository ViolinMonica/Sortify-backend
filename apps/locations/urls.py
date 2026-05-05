from django.urls import path
from .views import LocationListView, LocationCitiesView

urlpatterns = [
    path("", LocationListView.as_view(), name="location-list"),
    path("cities/", LocationCitiesView.as_view(), name="location-cities"),
]
