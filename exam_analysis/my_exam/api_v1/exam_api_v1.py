# my_exam/api_v1/exam_api_v1.py
from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/exams")
def get_exams():
    return {"exams": ["exam1", "exam2", "exam3"]}
