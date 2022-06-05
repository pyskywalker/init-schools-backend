from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import Response
from .models import *
from .serializers import CourseSerializer, InstructorSerializer, StudentSerializer,SingleInstructorSerializer,CourseOutlineItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StudentAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=PageNumberPagination

class InstructorAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Instructor.objects.all()
    serializer_class=InstructorSerializer
    pagination_class=PageNumberPagination

class CourseAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseOutlineAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=CourseOutline.objects.all()
    serializer_class=CourseSerializer

class CourseOutlineItemTypeAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=CourseOutline.objects.all()
    serializer_class=CourseSerializer

class CourseOutlineItemsAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CourseOutlineItemSerializer
    def get(self,request,id):
        courses= CourseItems.objects.filter(course_outline=id)
        serializer=CourseOutlineItemSerializer(courses,many=True)
        return Response(serializer.data)
    
class SingleInstructorAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Instructor.objects.all()
    serializer_class=SingleInstructorSerializer
    lookup_url_kwarg="id"

class SingleStudentAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Student.objects.all()
    lookup_url_kwarg="id"

class SingleCourseAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Course.objects.all()
    lookup_url_kwarg="id"
    serializer_class=CourseSerializer


######################FUNCTION BASED VIEW PAGINATION LOGIC##############################
# @api_view(['GET',])

# @permission_classes([AllowAny,])

# def PersonView(request):

#     paginator = PageNumberPagination()
#     paginator.page_size = 10
#     person_objects = Person.objects.all()
#     result_page = paginator.paginate_queryset(person_objects, request)
#     serializer = PersonSerializer(result_page, many=True)
#     return paginator.get_paginated_response(serializer.data)