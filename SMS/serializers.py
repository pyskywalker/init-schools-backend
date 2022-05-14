from rest_framework import serializers
from .models import *
from Users.models import MainUser as User
from Users.serializers import UserSerializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields="__all__"
class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model=NextOfKin
        fields="__all__"
class StudentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model= Student
        fields="__all__"
    
    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = User.objects.create(**user_data)
    #     user.is_student=True
    #     user.save()
    #     student=Student.object.create(user=user,**validated_data)
    #     student.save()
    #     return student
