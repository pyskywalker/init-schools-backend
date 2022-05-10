from rest_framework import serializers
from .models import *
from Users.models import MainUser as User
from Users.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model= Student
        fields="__all__"
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.is_student=True
        user.save()
        student=Student.object.create(user=user,**validated_data)
        student.save()
        return student
