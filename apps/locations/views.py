from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer


class LocationListView(APIView):
    """
    GET /api/v1/locations/?city=depok&type=BANK_SAMPAH&category=Plastik
    Filter TPS berdasarkan kota, tipe fasilitas, atau kategori sampah.
    """

    def get(self, request):
        city = request.query_params.get("city", "").strip()
        facility_type = request.query_params.get("type", "").strip()
        category = request.query_params.get("category", "").strip()

        qs = Location.objects.filter(is_active=True)

        if city:
            qs = qs.filter(city__icontains=city)
        if facility_type:
            qs = qs.filter(facility_type=facility_type)
        if category:
            # Filter lokasi yang menerima kategori ini
            qs = [loc for loc in qs if category in loc.accepts_categories]

        # Jika pakai queryset murni (tanpa category filter)
        if not category:
            serializer = LocationSerializer(qs, many=True)
        else:
            serializer = LocationSerializer(qs, many=True)

        return Response({
            "success": True,
            "count": len(serializer.data),
            "filters": {
                "city": city or None,
                "type": facility_type or None,
                "category": category or None,
            },
            "locations": serializer.data,
        })


class LocationCitiesView(APIView):
    """GET /api/v1/locations/cities/ — daftar kota yang tersedia"""

    def get(self, request):
        cities = (
            Location.objects.filter(is_active=True)
            .values_list("city", flat=True)
            .distinct()
            .order_by("city")
        )
        return Response({
            "success": True,
            "cities": list(cities),
        })
