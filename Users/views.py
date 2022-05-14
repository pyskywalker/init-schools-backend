from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import MainUser
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin

from .permissions import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from django.contrib.auth import     login
# Create your views here.


class UserList(generics.ListCreateAPIView):
    permission_classes=[OwnerEditStaffReadAndCreate]
    queryset=MainUser.objects.all()
    serializer_class=UserSerializer

class UserRolesAPI(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=UserRole.objects.all()
    serializer_class=UserRoleSerializer
class RegisterAPI():
    pass


class ChangePassword(APIView):
    def post(request):
        u = MainUser.objects.get(username=request.user.username)
        u.set_password(request.post["password1"])
        u.save()


        