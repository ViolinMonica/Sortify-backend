# Sortify Backend Structure

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
