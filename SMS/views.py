from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StudentAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=PageNumberPagination


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