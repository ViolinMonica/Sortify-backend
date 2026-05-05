import numpy as np
from PIL import Image
import io
import os
from django.conf import settings

_model = None

CLASS_LABELS = [
    "battery",
    "biological",
    "cardboard",
    "clothes",
    "glass",
    "metal",
    "paper",
    "plastic",
    "shoes",
    "trash",
]

SORTIFY_CATEGORIES = {
    "B3":      ["battery"],
    "Organic": ["biological"],
    "Paper":   ["cardboard", "paper"],
    "Textile": ["clothes", "shoes"],
    "Glass":   ["glass"],
    "Metal":   ["metal"],
    "Plastic": ["plastic"],
    "Residue": ["trash"],
}

LABEL_TO_CATEGORY = {
    label: category
    for category, labels in SORTIFY_CATEGORIES.items()
    for label in labels
}

def get_model():
    """Lazy load model so startup is faster."""
    global _model
    if _model is None:
        try:
            import tensorflow as tf
            model_path = settings.AI_MODEL_PATH
            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"Model not found at: {model_path}\n"
                    f"Make sure the .keras file is placed at the correct path."
                )
            _model = tf.keras.models.load_model(model_path)
            print(f"[Sortify AI] Model successfully loaded from: {model_path}")
        except ImportError:
            raise ImportError("TensorFlow is not installed. Run: pip install tensorflow")
    return _model


def preprocess_image(image_file, target_size=(224, 224)):
    """
    Preprocess image for MobileNet model input.
    MobileNet input: (224, 224, 3), normalized [0, 1]
    """
    img = Image.open(image_file).convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # (1, 224, 224, 3)
    return img_array


def classify_image(image_file):
    """
    Classify waste image.
    
    Returns:
        dict: {
            "raw_label": "plastic",           # original label from model
            "sortify_category": "Plastic",    # Sortify category
            "confidence": 0.94,               # confidence score
            "all_scores": {...}               # all labels and their scores
        }
    """
    model = get_model()
    img_array = preprocess_image(image_file)
    
    predictions = model.predict(img_array, verbose=0)
    scores = predictions[0]  # shape: (num_classes,)
    
    top_index = int(np.argmax(scores))
    top_label = CLASS_LABELS[top_index]
    top_confidence = float(scores[top_index])
    
    all_scores = {
        CLASS_LABELS[i]: round(float(scores[i]), 4)
        for i in range(len(CLASS_LABELS))
    }
    
    return {
        "raw_label": top_label,
        "sortify_category": LABEL_TO_CATEGORY.get(top_label, "Residue"),  
        "confidence": round(top_confidence, 4),
        "all_scores": all_scores,
    }