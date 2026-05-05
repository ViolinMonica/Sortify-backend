from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "facility_type", "city", "province", "is_active"]
    list_filter = ["facility_type", "city", "is_active"]
    search_fields = ["name", "city", "address"]
