from dataclasses import field
from rest_framework import serializers
from .models import *
from Users.models import MainUser as User
from Users.serializers import UserSerializer,ContactsSerializer

    
class NextOfKinSerializer(serializers.ModelSerializer):
    contacts=ContactsSerializer(many=True)
    class Meta:
        model=NextOfKin
        fields="__all__"
class CourseWithoutSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"

class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model=School
        fields="__all__"

class SubjectSerializer(serializers.ModelSerializer):
    course_subjects=CourseWithoutSubjectSerializer(many=True,read_only=True)
    class Meta:
        model=Subjects
        fields="__all__"
    
class CourseSerializer(serializers.ModelSerializer):
    subjects=SubjectSerializer(many=True,read_only=True)
    class Meta:
        model=Course
        fields="__all__"

class SingleInstructorSerializer(serializers.ModelSerializer):
    user_id=UserSerializer()
    subjects=SubjectSerializer(many=True)
    next_of_kin=NextOfKinSerializer()
    branch=BranchSerializer(many=True)
    class Meta:
        model=Instructor
        fields="__all__"

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Subjects
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

class InstructorSerializer(serializers.ModelSerializer):
    user_id=UserSerializer()
    class Meta:
        model= Instructor
        fields="__all__"
    
    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = User.objects.create(**user_data)
    #     user.is_student=True
    #     user.save()
    #     student=Student.object.create(user=user,**validated_data)
    #     student.save()
    #     return student
