from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    facility_type_display = serializers.CharField(
        source="get_facility_type_display", read_only=True
    )

    class Meta:
        model = Location
        fields = [
            "id",
            "name",
            "facility_type",
            "facility_type_display",
            "city",
            "province",
            "address",
            "latitude",
            "longitude",
            "phone",
            "maps_url",
        ]
