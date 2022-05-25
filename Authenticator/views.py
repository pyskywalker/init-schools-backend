from django.shortcuts import render
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from Users.models import MainUser, Permissions
from rest_framework.views import APIView
from .models import Token
from Users.serializers import UserSerializer
from .utils import CsrfExemptSessionAuthentication
from .authentication import ExpiringTokenAuthentication
# 
# Create your views here.

class SingleUser(APIView):
    def get(self,request):
        token=request.headers['Authorization'].split()
        full=Token.objects.get(key=token[1])
        user=UserSerializer(full.user)
        return Response(user.data)

class LoginAPI(ObtainAuthToken):
     authentication_classes = (CsrfExemptSessionAuthentication, ExpiringTokenAuthentication)
     permission_classes=[AllowAny,]
     def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        newPassword=request.data['password']
        print(newPassword)
        mainuser=MainUser.objects.get(username=user.username)
        oneuser=UserSerializer(MainUser.objects.get(username=user.username))
        if Token.objects.filter(user=user).exists():
            Token.objects.get(user=user).delete()
        token,created= Token.objects.get_or_create(user=user)
        mainuser.last_login=timezone.now()
        mainuser.save()
        return Response({
            'token': token.key,
            'is_created':created,
            'user':oneuser.data,

        })

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