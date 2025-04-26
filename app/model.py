from typing import List, Dict
from PIL import Image

def predict(image: Image.Image) -> List[Dict[str, float]]:
    """
    Dummy prediction function for food recognition.
    Replace this stub with real model inference logic.
    """
    # TODO: implement real model inference
    return [
        {"label": "pizza", "score": 0.9},
        {"label": "burger", "score": 0.1},
    ]