from django.urls import path

from SMS.models import Student
from .views import StudentAPI
urlpatterns=[path('students',StudentAPI.as_view(),name="student-list"),]