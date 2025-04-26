# 🍎 Food Detection Web App

This is a **full-stack machine learning app** that allows you to upload a food image and receive a prediction of what it is.

Built with:
- **FastAPI** (backend API)
- **React** (frontend interface)
- **PyTorch** (image classification model)

---

## 🚀 Local Development Setup

Follow these steps to get the project running locally:

### 1. Backend Setup (FastAPI)

1. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

Server will run on [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 2. Frontend Setup (React)

1. Open a new terminal tab/window.
2. Navigate to the frontend project directory:

    ```bash
    cd frontend
    ```

3. Install frontend dependencies:

    ```bash
    npm install
    ```

4. Start the React development server:

    ```bash
    npm run dev
    ```

Frontend will run on [http://127.0.0.1:5173](http://127.0.0.1:5173) (default Vite dev server port).

---

## 🛠 How it Works

- The **frontend** allows you to upload a food image.
- The **backend API** accepts the image at the `/predict` endpoint, runs it through a simple **ResNet-based model**, and returns a **predicted food label**.
- The frontend displays the prediction instantly.

---

## 📸 API Endpoints

| Method | Endpoint      | Description                          |
|:------|:---------------|:-------------------------------------|
| GET   | `/`            | Health check                        |
| POST  | `/predict`     | Accepts an image file, returns label |

POST `/predict` expects `form-data` with a field named `file`.

Example request (if testing manually):

```bash
curl -X POST "http://127.0.0.1:8000/predict" -F "file=@path_to_your_image.jpg"
```

---

## 🧪 Testing

Run backend tests with:

```bash
pytest
```

---

## ✨ Next Improvements

- Fine-tune the model for better prediction accuracy.
- Add loading spinners and error handling on the frontend.
- Deploy the backend and frontend for public access.
- Improve UI styling and mobile responsiveness.

---

## ⚡ Quick Start Summary

```bash
# In one terminal (backend)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# In another terminal (frontend)
cd frontend
npm install
npm run dev
```

Then open [http://127.0.0.1:5173](http://127.0.0.1:5173) in your browser!

---

Built with love ❤️ by [James Bateman]