from django.urls import path, include
from rest_framework.routers import DefaultRouter
from my_exam.views import ExamViewSet  # Import your view

# Create a router and register the Exam viewset
router = DefaultRouter()
router.register(r'exams', ExamViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),  # This sets up the /api/v1/exams/ endpoint
]
