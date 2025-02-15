# my_exam/api_v1/exam_api_v1.py
from fastapi import APIRouter, HTTPException
# from controllers.rrb_je_controller import RRBJEController  # Import the controller
from my_exam.controllers.rrb_je_controller import RRBJEController
from my_exam.controllers.ssc_exam_controller import SSCExamController
from my_exam.schema import ScrapeRequest 

api_router = APIRouter()

@api_router.get("/exams")
def get_exams():
    return {"exams": ["exam1", "exam2", "exam3"]}

@api_router.post("/scrape-exam-data")
def scrape_exam_data(request:ScrapeRequest):
    try:
        data = RRBJEController.fetch_exam_data(
            request.url, request.category, request.Horizontalcategory,
            request.Exam_Language, request.RRB_zone, request.RRB_branch
        )
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred in railway: {str(e)}")
    # url = "https://rrb.digialm.com//per/g22/pub/1907/touchstone/AssessmentQPHTMLMode1//1907O245/1907O245S8D16147/17346759348902617/153244130886756_1907O245S8D16147E1.html"
    # data = RRBJEController.fetch_exam_data(url)  # Call the scraper controller
    # return data
    
@api_router.post("/ssc-exam-data")
def scrape_exam_data(request:ScrapeRequest):
    try:
        data = SSCExamController.fetch_ssc_exam_data(
            request.url, request.category, request.Horizontalcategory,
            request.Exam_Language, request.exam_type
        )
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred in ssc: {str(e)}")

