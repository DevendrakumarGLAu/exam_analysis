# my_exam/api_v1/exam_api_v1.py
from fastapi import APIRouter
# from controllers.rrb_je_controller import RRBJEController  # Import the controller
from my_exam.controllers.rrb_je_controller import RRBJEController

api_router = APIRouter()

@api_router.get("/exams")
def get_exams():
    return {"exams": ["exam1", "exam2", "exam3"]}

@api_router.get("/scrape-exam-data")
def scrape_exam_data():
    url = "https://rrb.digialm.com//per/g22/pub/1907/touchstone/AssessmentQPHTMLMode1//1907O245/1907O245S8D16147/17346759348902617/153244130886756_1907O245S8D16147E1.html"
    data = RRBJEController.fetch_exam_data(url)  # Call the scraper controller
    return data
