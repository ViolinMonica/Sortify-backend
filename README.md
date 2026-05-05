# Sortify Backend
One photo. Right Disposal.
Django REST API untuk klasifikasi sampah dan rekomendasi pembuangan.
## Setup, panduan menjalankan Sortify backend di lokal
Pastikan sudah terinstall:
Python 3.11 (wajib, untuk kompatibilitas TensorFlow)
Link instalasi: https://www.python.org/downloads/release/python-3110/

# 1. Clone repo
```
git clone https://github.com/ViolinMonica/Sortify-backend.git
cd Sortify-backend
```

# 2. Buat virtual environment (Opsional, jika sebelumnya sudah pernah terinstall python yang bukan versi 3.9, 3.10, 3.11, atau 3.12)
# Windows
```
py -3.11 -m venv venv
venv311\Scripts\activate
```

# Mac/Linux
```
python3.11 -m venv venv
source venv/bin/activate
```
# 3. Pindah ke folder Uni/IYREF 2025/sortify_backend
``` 
cd Uni/IYREF 2026/sortify_backend
```

# 4. Install dependencies
```
pip install -r requirements.txt
```

# 5. Download model
Folder models/ tidak disertakan di repo. Download modelnya di sini: https://drive.google.com/drive/folders/1MKT8-WK_tW45N8s0SLpqf6RH2JFBu1ld?usp=sharing dan unzip filenya.
Letakkan di root folder sortify_backend:
```
sortify_backend/
└── models/
    └── model.weights.h5
    └── config.json
    └── metadata.json
```

# 6. Buat file .env berisi:
```
SECRET_KEY=<your-secret-key-here> #Masukkan secret key yang diinginkan
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
AI_MODEL_PATH=./models
MAX_UPLOAD_SIZE_MB=10
```

# 6. Jalankan migrasi
```
python manage.py migrate
```

# 7. Seed data TPS
```
python scripts/seed_locations.py
```

# 8. Jalankan server
python manage.py runserver
```

## API Endpoints

### Klasifikasi Sampah
```
POST /api/classify/
Content-Type: multipart/form-data

Body: image (file) — foto sampah (jpg/png/webp)

```
Response:
{
  "success": true,
  "classification": {
    "category": "Plastik",
    "raw_label": "plastic",
    "confidence": 0.94
  },
  "recommendation": {
    "category": "Plastik",
    "description": "...",
    "disposal_instructions": [...],
    "penanganan": { "label": "...", "video_url": "..." },
    "facility": { "label": "...", "type": "BANK_SAMPAH" }
  }
}
```

### Rekomendasi Sampah
```
GET /api/waste/                    → all categories
GET /api/waste/Plastic/            → per category
GET /api/waste/Paper/
GET /api/waste/Glass/
GET /api/waste/Organic/
GET /api/waste/Metal/
GET /api/waste/Residue/
GET /api/waste/B3/
GET /api/waste/Textile/
```

### Lokasi TPS
```
GET /api/locations/                          → semua lokasi
GET /api/locations/?city=Depok               → filter by kota
GET /api/locations/?type=BANK_SAMPAH         → filter by tipe
GET /api/locations/?category=Plastik         → filter by kategori sampah
GET /api/locations/cities/                   → daftar kota tersedia
```

## Struktur project
```
sortify_backend/
├── manage.py
├── requirements.txt
├── model/                    # model AI
│   ├── config.json
│   ├── metadata.json
│   └── model.weights.h5
├── sortify/                    # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── classifier/             # AI classification
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── serializers.py
│   │   └── ai_service.py       # load .keras & predict
│   ├── waste/                  # Rekomendasi buang sampah
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── serializers.py
│   │   └── recommendation.py  # rule-based engine
│   └── locations/             # TPS terdekat
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── serializers.py
│       └── data/tps_data.json  # data TPS statis
└── scripts/
    └── seed_locations.py       # seed TPS ke DB
```

## Kategori Sampah & Mapping
| Label Model        | Kategori Sortify |
|--------------------|------------------|
| battery            | B3               |
| biological         | Organik          |
| cardboard, paper   | Kertas           |
| clothes, shoes     | Tekstil          |
| glass              | Kaca             |
| metal              | Logam            |
| plastic            | Plastik          |
| trash              | Residu           |
