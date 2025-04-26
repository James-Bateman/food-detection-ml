from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.model import load_model, predict_image
from PIL import Image
import io

router = APIRouter()

model, transform, class_names = load_model()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert('RGB')
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    prediction = predict_image(image, model, transform, class_names)
    return {"prediction": prediction}
