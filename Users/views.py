from django.shortcuts import render
from rest_framework import generics
from .models import MainUser
from .serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.


class UserList(PermissionRequiredMixin,generics.ListCreateAPIView):
    permission_required='user.view_user'
    raise_exception=True
    queryset=MainUser.objects.all()
    serializer_class=UserSerializer
