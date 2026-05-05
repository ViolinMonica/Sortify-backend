from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .recommendation import get_recommendation, RECOMMENDATIONS


class RecommendationListView(APIView):
    """GET /api/waste/ — daftar semua kategori + rekomendasi"""

    def get(self, request):
        return Response({
            "success": True,
            "categories": list(RECOMMENDATIONS.values()),
        })


class RecommendationDetailView(APIView):
    """GET /api/waste/<category>/ — rekomendasi spesifik per kategori"""

    def get(self, request, category):
        # Normalize input (case-insensitive)
        normalized = category.strip().title()
        recommendation = RECOMMENDATIONS.get(normalized)

        if not recommendation:
            valid = list(RECOMMENDATIONS.keys())
            return Response(
                {
                    "error": f"Kategori '{category}' tidak ditemukan.",
                    "valid_categories": valid,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response({"success": True, "recommendation": recommendation})
