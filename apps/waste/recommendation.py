"""
Recommendation Engine - Rule-based mapping of waste categories → disposal instructions.
Can be updated without changing the AI model.
"""

RECOMMENDATIONS = {
    "Organic": {
        "category": "Organic",
        "description": "Leftover food, leaves, or natural materials that decompose easily.",
        "disposal_instructions": [
            "Dispose in the organic waste bin (green).",
            "Can be composted at home.",
            "Do not mix with plastic or glass waste.",
        ],
        "penanganan": {
            "label": "Self-Recycling",
            "description": "Make compost from your organic waste.",
            "video_url": "https://www.youtube.com/embed/39vgpoFMTYM?si=V8q1ifDZ98hlAKWG",
        },
        "facility": {
            "label": "Nearest Facility",
            "description": "Find a waste bank or TPS that accepts organic waste.",
            "type": "TPS_ORGANIK",
        },
    },

    "Plastic": {
        "category": "Plastic",
        "description": "Bottles, bags, packaging, or plastic items.",
        "disposal_instructions": [
            "Rinse before disposing to avoid odor.",
            "Dispose in the inorganic waste bin (yellow/blue).",
            "Can be sold to the nearest waste bank.",
        ],
        "penanganan": {
            "label": "Self-Recycling",
            "description": "Plastic can be turned into handicrafts.",
            "video_url": "https://www.youtube.com/embed/videoseries?si=SJH5Tkjg9qZVanEn&list=PLE-Pmp3rd5KCo9cA2gk3gr0rWxy12W2E9",
        },
        "facility": {
            "label": "Nearest Facility",
            "description": "Waste banks accept clean and dry plastic.",
            "type": "BANK_SAMPAH",
        },
    },

    "Paper": {
        "category": "Paper",
        "description": "Cardboard, used boxes, paper, newspapers, or paper-based packaging.",
        "disposal_instructions": [
            "Make sure it is dry and not contaminated with food.",
            "Flatten cardboard boxes to save space.",
            "Collect and sell to a collector or waste bank.",
        ],
        "penanganan": [
            {
                "label": "Self-Recycling (Cardboard)",
                "description": "Cardboard can be turned into shelves, children's toys, or multipurpose boxes.",
                "video_url": [
                    "https://www.youtube.com/embed/qMCZY8MhJ_Y?si=e7ABaFUoKG58jlwA",
                    "https://www.youtube.com/embed/wOyhfpKREMA?si=bh4Xlrk6095G1Jtj",
                ],
            },
            {
                "label": "Self-Recycling (Paper)",
                "description": "Used paper can be turned into crafts or new notebooks.",
                "video_url": [
                    "https://www.youtube.com/embed/5xrWrKIVBgo?si=AasSFKyKDk5D75Wi",
                    "https://www.youtube.com/embed/videoseries?si=6KuxvDsdUxm2iYlE&list=PLt5I7eZUkp9vzf60hAeyUQwe0jO3ru7tq",
                    "https://www.youtube.com/embed/lT-VgG3CN2s?si=Fd3SiWkWaPSqJh73",
                ],
            },
        ],
        "facility": {
            "label": "Nearest Facility",
            "description": "Waste banks and paper collectors accept cardboard and newspapers.",
            "type": "BANK_SAMPAH",
        },
    },

    "Glass": {
        "category": "Glass",
        "description": "Glass bottles, jars, or broken glass.",
        "disposal_instructions": [
            "Wrap broken glass in newspaper before disposing for safety.",
            "Whole glass bottles can be returned to stores or sold.",
            "Do not dispose in regular trash without wrapping.",
        ],
        "penanganan": {
            "label": "Self-Recycling",
            "description": "Glass bottles can be reused as containers or decorations.",
            "video_url": "https://www.youtube.com/embed/Ny8Af_ADvtg?si=a6ChM93isy0F8G_M",
        },
        "facility": {
            "label": "Nearest Facility",
            "description": "Find a waste bank or collector that accepts glass.",
            "type": "BANK_SAMPAH",
        },
    },

    "Metal": {
        "category": "Metal",
        "description": "Cans, scrap iron, or other metal waste.",
        "disposal_instructions": [
            "Metal/scrap iron is non-hazardous waste that can be recycled.",
            "Collect and sell to the nearest scrap metal collector.",
            "Beverage cans: rinse first, then sell to a waste bank.",
            "⚠️ If it is industrial slag, contact a hazardous waste manager.",
        ],
        "penanganan": {
            "label": "Self-Recycling",
            "description": "Used cans can be turned into plant pots or storage containers.",
            "article_url": "https://www.hipwee.com/tips/11-daur-ulang-kaleng-bekas/",
        },
        "facility": {
            "label": "Nearest Facility",
            "description": "Scrap metal collectors or waste banks that accept metal.",
            "type": "PENGEPUL_LOGAM",
        },
    },

    "Residue": {
        "category": "Residue",
        "description": "Mixed waste that cannot be recycled (styrofoam, multi-layered packaging, etc).",
        "disposal_instructions": [
            "Dispose in the residue/mixed waste bin.",
            "This waste will be taken to the final disposal site (TPA).",
            "Reduce consumption of similar products in the future.",
        ],
        "penanganan": {
            "label": "Reduction Tips",
            "description": "Avoid products with multi-layered or hard-to-recycle packaging.",
            "article_url": "https://desanaob.id/cara-mengurangi-sampah-rumah-tangga-2026/",
        },
        "facility": {
            "label": "Nearest Facility",
            "description": "Nearest temporary disposal site (TPS) in your city.",
            "type": "TPS",
        },
    },

    "B3": {
        "category": "Hazardous Waste",
        "description": "Hazardous and toxic waste such as batteries, lamps, expired medicine, household chemicals, and electronic waste.",
        "disposal_instructions": [
            "Separate from household waste from the start.",
            "Do not dispose in regular trash or waterways.",
            "Store in a sealed container to prevent leaks or environmental contamination.",
            "Collect and bring to a hazardous waste facility or e-waste drop box.",
            "For batteries and electronics, avoid exposure to water or excessive heat.",
        ],
        "penanganan": {
            "label": "Hazardous Waste Education",
            "description": "Learn how to safely and properly dispose of household hazardous waste.",
            "article_url": "https://www.limbah.id/blog/cara-mengelola-limbah-b3-dengan-aman-dan-sesuai-regulasi/",
        },
        "facility": {
            "label": "Nearest Facility",
            "description": "E-waste drop box or official hazardous waste management facility.",
            "type": "B3",
        },
    },

    "Textile": {
        "category": "Textile",
        "description": "Used clothing, fabric, or footwear.",
        "disposal_instructions": [
            "Check the condition: still wearable or not?",
            "If still wearable, donate to a social foundation or nearest donation box.",
            "If no longer wearable, dispose at TPS as residue.",
            "Do not throw into drains or litter.",
        ],
        "penanganan": [
            {
                "label": "Self-Recycling (Fabric)",
                "description": "Used clothes can be upcycled into various cool new items!",
                "video_url": "https://www.youtube.com/embed/CY0qaRRyKHo?si=NV5p890dZBqVSmi6",
            },
            {
                "label": "Self-Recycling (Shoes)",
                "description": "Used shoes of all kinds can be repaired, repainted, or redesigned into a cool new look.",
                "video_url": "https://www.youtube.com/embed/MXvHItMx2KY?si=WTPGxEPf-5hfdkYZ",
            },
            {
                "label": "Self-Donation (Fabric)",
                "description": "Wearable clothes can be donated through various trusted donation platforms in Indonesia.",
                "article_url": "https://odesa.id/7-platform-donasi-baju-bekas-yang-terpercaya/",
            },
            {
                "label": "Self-Donation (Shoes)",
                "description": "Wearable shoes can be donated to secondhand donation platforms such as Donasi Barang.",
                "article_url": "https://donasibarang.id/",
            },
        ],
        "facility": {
            "label": "Nearest Facility",
            "description": "Nearest TPS for clothing or shoes that are no longer wearable.",
            "type": "TPS",
        },
    },
}


def get_recommendation(sortify_category: str, raw_label: str = None) -> dict:
    rec = RECOMMENDATIONS.get(sortify_category, RECOMMENDATIONS["Residue"])

    if sortify_category == "Textile" and raw_label in ("clothes", "shoes"):
        filtered = rec.copy()
        if raw_label == "clothes":
            filtered["penanganan"] = [
                p for p in rec["penanganan"]
                if "Shoes" not in p["label"]
            ]
        elif raw_label == "shoes":
            filtered["penanganan"] = [
                p for p in rec["penanganan"]
                if "Fabric" not in p["label"]
            ]
        return filtered

    if sortify_category == "Paper" and raw_label in ("cardboard", "paper"):
        filtered = rec.copy()
        if raw_label == "cardboard":
            filtered["penanganan"] = [
                p for p in rec["penanganan"]
                if "Paper" not in p["label"]
            ]
        elif raw_label == "paper":
            filtered["penanganan"] = [
                p for p in rec["penanganan"]
                if "Cardboard" not in p["label"]
            ]
        return filtered

    return rec