import os
import django
from fastapi import FastAPI
from my_exam.api_v1.exam_api_v1 import api_router  # Ensure this import is correct!


# ✅ Initialize Django BEFORE importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam_analysis.settings")
django.setup()

# ✅ Now, import API router AFTER Django setup
from my_exam.api_v1.exam_api_v1 import api_router

app = FastAPI(title="Exam API")


app.include_router(api_router, prefix="/api/v1")  # Ensure the prefix is set to '/api/v1'

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}
