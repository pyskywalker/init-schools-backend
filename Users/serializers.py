from rest_framework import serializers
from .models import MainUser,UserRole,Permissions

class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Permissions
        exclude=["created_at","modified_at"]

class UserRoleSerializer(serializers.ModelSerializer):
    permission=PermissionSerializers(many=True)
    class Meta:
        model=UserRole
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    user_roles=UserRoleSerializer(many=True,read_only=True)
    class Meta:
        model=MainUser
        exclude=['password']