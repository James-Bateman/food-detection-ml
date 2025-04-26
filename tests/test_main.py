import io

import pytest
from PIL import Image
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Food Recognition API"}

def test_predict_invalid_file():
    # send invalid image data
    response = client.post(
        "/predict",
        files={"file": ("test.jpg", b"notanimage", "image/jpeg")},
    )
    assert response.status_code == 400
    assert "error" in response.json()

def test_predict_valid_file():
    # create a small valid image in memory
    img = Image.new("RGB", (10, 10), color=(255, 0, 0))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)
    response = client.post(
        "/predict",
        files={"file": ("test.jpg", buf.read(), "image/jpeg")},
    )
    assert response.status_code == 200
    data = response.json()
    assert "predictions" in data
    assert isinstance(data["predictions"], list)