from django.shortcuts import render
from rest_framework import generics
from .models import MainUser
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.authtoken.views import ObtainAuthToken
from .permissions import *
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from django.contrib.auth import     login
# Create your views here.


class UserList(generics.ListCreateAPIView):
    permission_classes=[OwnerEditStaffReadAndCreate]
    queryset=MainUser.objects.all()
    serializer_class=UserSerializer
class RegisterAPI():
    pass
class LoginAPI(ObtainAuthToken):
     permission_classes=[AllowAny,]
     def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        newPassword=request.data['password']
        print(newPassword)
        mainuser=MainUser.objects.get(username=user.username)
        token,created= Token.objects.get_or_create(user=user)
        mainuser.last_login=timezone.now()
        mainuser.save()
        return Response({
            'token': token.key,
            'is_created':created,
            'user_id': user.pk,
            'user_first_name':user.first_name,
            'user_last_name':user.last_name,
            'user_username':user.username,
            'email': user.email
        })

class ChangePassword(APIView):
    def post(request):
        u = MainUser.objects.get(username=request.user.username)
        u.set_password(request.post["password1"])
        u.save()

class LoginCustom(APIView):
    permission_classes=[AllowAny,]
    def post(self,request):
        username=request.data['username']
        password=request.data['password']
        try:
            user=MainUser.objects.get(username=username)
        except BaseException as e:
            return Response(
                {"400":f"{str(e)}"}
            )
        token,created= Token.objects.get_or_create(user=user)
        print(token)
        if not check_password(password,user.password):
            return Response({
                "message": "Incorrect Login credentials"
            })
        if user:
            if user.is_active:
                print(request.user)
                login(request,user)
                return Response(
                    {
                    'token': token.key,
                    'is_created':created,
                    'user_id': user.pk,
                    'user_first_name':user.first_name,
                    'user_last_name':user.last_name,
                    'user_username':user.username,
                    'email': user.email
                     }
                )
        