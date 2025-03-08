import os
import django
from fastapi import FastAPI
from my_exam.api_v1.exam_api_v1 import api_router  # Ensure this import is correct!
from fastapi.middleware.cors import CORSMiddleware


# ✅ Initialize Django BEFORE importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam_analysis.settings")
django.setup()

# ✅ Now, import API router AFTER Django setup
from my_exam.api_v1.exam_api_v1 import api_router

app = FastAPI(title="Exam API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods: GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allow all headers
)

app.include_router(api_router, prefix="/api/v1")  # Ensure the prefix is set to '/api/v1'

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}
