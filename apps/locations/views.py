import math
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer


def haversine(lat1, lon1, lat2, lon2):
    """Hitung jarak antara dua koordinat dalam km."""
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    return R * 2 * math.asin(math.sqrt(a))


def get_nearest(locations, lat, lng, n=3):
    """Ambil n lokasi terdekat dari koordinat user."""
    for loc in locations:
        loc._distance_km = round(haversine(lat, lng, loc.latitude, loc.longitude), 2)
    return sorted(locations, key=lambda loc: loc._distance_km)[:n]


def serialize_with_distance(locations):
    """Serialize lokasi + inject distance_km."""
    serializer = LocationSerializer(locations, many=True)
    result = list(serializer.data)
    for i, loc in enumerate(locations):
        result[i]["distance_km"] = loc._distance_km
    return result


class LocationListView(APIView):
    """
    GET /api/v1/locations/
    Filter manual: ?city=depok&type=BANK_SAMPAH
    """

    def get(self, request):
        city = request.query_params.get("city", "").strip()
        facility_type = request.query_params.get("type", "").strip()

        qs = Location.objects.filter(is_active=True)

        if city:
            qs = qs.filter(city__icontains=city)
        if facility_type:
            qs = qs.filter(facility_type=facility_type)

        serializer = LocationSerializer(qs, many=True)
        return Response({
            "success": True,
            "count": len(serializer.data),
            "filters": {
                "city": city or None,
                "type": facility_type or None,
            },
            "locations": serializer.data,
        })


class LocationNearestView(APIView):
    """
    GET /api/v1/locations/nearest/?lat=-6.37&lng=106.83
    Return 3 terdekat per facility type: BANK_SAMPAH, TPS, TPST
    """

    def get(self, request):
        lat = request.query_params.get("lat")
        lng = request.query_params.get("lng")

        if not lat or not lng:
            return Response(
                {"error": "Parameter lat dan lng wajib diisi."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            lat = float(lat)
            lng = float(lng)
        except ValueError:
            return Response(
                {"error": "lat dan lng harus berupa angka."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        all_locations = list(Location.objects.filter(is_active=True))

        facility_types = ["BANK_SAMPAH", "TPS", "TPST", "TPA"]
        result = {}

        for ftype in facility_types:
            filtered = [loc for loc in all_locations if loc.facility_type == ftype]
            nearest = get_nearest(filtered, lat, lng, n=3)
            result[ftype.lower()] = serialize_with_distance(nearest)

        return Response({
            "success": True,
            "user_location": {"lat": lat, "lng": lng},
            "nearest": result,
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