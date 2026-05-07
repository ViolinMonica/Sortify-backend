from django.db import models


class Location(models.Model):
    FACILITY_TYPES = [
        ("BANK_SAMPAH", "Bank Sampah"),
        ("TPS", "Tempat Pembuangan Sementara"),
        ("TPS_ORGANIK", "TPS Organik"),
        ("PENGEPUL_LOGAM", "Pengepul Logam/Rongsokan"),
        ("TPA", "Tempat Pembuangan Akhir"),
    ]

    name = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=20, choices=FACILITY_TYPES)
    city = models.CharField(max_length=100, db_index=True)
    province = models.CharField(max_length=100, default="")
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, default="")
    maps_url = models.URLField(blank=True, default="")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["city", "name"]

    def __str__(self):
        return f"{self.name} - {self.city}"
