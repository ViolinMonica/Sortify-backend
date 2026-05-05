from django.urls import path
from .views import RecommendationListView, RecommendationDetailView

urlpatterns = [
    path("", RecommendationListView.as_view(), name="waste-list"),
    path("<str:category>/", RecommendationDetailView.as_view(), name="waste-detail"),
]
