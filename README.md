# Food Image Classification Web App

This is a FastAPI-based web application that lets you upload an image and returns predicted food labels.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `GET /` - Health check endpoint.
- `POST /predict` - Accepts form-data with field `file` containing the image. Returns JSON with predictions.

## Testing

Run tests with pytest:
```bash
pytest
```

## Next Steps

- Replace the dummy model in `app/model.py` with a real pretrained model.
 
## Frontend

A simple web frontend is available at `/ui`. Start the server:

```bash
uvicorn app.main:app --reload
```
Then open [http://localhost:8000/ui](http://localhost:8000/ui) in your browser to upload an image and see predictions.