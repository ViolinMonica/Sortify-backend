from django.urls import path
from .views import ClassifyView

urlpatterns = [
    path("", ClassifyView.as_view(), name="classify"),
]
