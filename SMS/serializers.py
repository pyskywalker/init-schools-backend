from dataclasses import field
from rest_framework import serializers
from .models import *
from Users.models import MainUser as User
from Users.serializers import UserSerializer,ContactsSerializer

    
class NextOfKinSerializer(serializers.ModelSerializer):
    contacts=ContactsSerializer(many=True,read_only=True)
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
class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Specializations
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

class CourseOutlineSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseOutline
        fields="__all__"

class CourseOutlineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseItemType
        fields="__all__"

class CourseOutlineItemSerializer(serializers.ModelSerializer):
    course_outline=CourseOutlineSerializer(read_only=True)
    course_item_type=CourseOutlineTypeSerializer(read_only=True)
    created_by=UserSerializer(read_only=True)
    class Meta:
        model=CourseItems
        fields="__all__"

class SingleInstructorSerializer(serializers.ModelSerializer):
    user_id=UserSerializer(read_only=True)
    specialization=SpecializationSerializer(read_only=True)
    subjects=SubjectSerializer(many=True,read_only=True)
    next_of_kin=NextOfKinSerializer(read_only=True)
    branch=BranchSerializer(many=True,read_only=True)
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
