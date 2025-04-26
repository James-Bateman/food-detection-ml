import io

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
from PIL import Image

from app.model import predict
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Food Recognition API")
# Serve static frontend assets
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")),
    name="static",
)

@app.get("/ui", response_class=HTMLResponse)
async def get_ui():
    """Serve the frontend UI."""
    file_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return HTMLResponse(status_code=404, content="UI not found")

@app.get("/")
async def root():
    return {"message": "Food Recognition API"}

@app.post("/predict")
async def predict_food(file: UploadFile = File(...)):
    """
    Accept an uploaded image file and return food predictions.
    """
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        return JSONResponse(status_code=400, content={"error": "Invalid image file"})
    results = predict(image)
    return {"predictions": results}