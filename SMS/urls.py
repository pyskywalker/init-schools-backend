from django.urls import path

from SMS.models import Student
from .views import CourseAPI, CourseOutlineAPI, CourseOutlineItemsAPI, InstructorAPI, SingleStudentAPI, StudentAPI,SingleInstructorAPI,SingleCourseAPI
urlpatterns=[
    path('students',StudentAPI.as_view(),name="student-list"),
    path('instructor',InstructorAPI.as_view(),name="instructor-list"),
path('student',SingleStudentAPI.as_view(),name="student"),
path('instructor/<int:id>',SingleInstructorAPI.as_view(),name="single-instructor"),
path('course/<int:id>',SingleCourseAPI.as_view(),name="single-course"),
path('course',CourseAPI.as_view(),name="course"),
path('course-outline-items/<int:id>',CourseOutlineItemsAPI.as_view(),name="course-outline-items"),

]