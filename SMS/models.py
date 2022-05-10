from django.db import models
from Users.models import MainUser,Location,Contacts
import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class School(models.Model):
    branch_name=models.CharField(max_length=100)
    location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    principal=models.ForeignKey(MainUser,on_delete=models.SET_NULL,null=True)
    contacts=models.ForeignKey(Contacts,on_delete=models.SET_NULL,null=True)
    is_active=models.BooleanField(default=True)

class Course(models.Model):
    course_code=models.CharField(max_length=10)
    course_name=models.CharField(max_length=100)
    school_year=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

class NextOfKin(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,null=True,blank=True)
    relationship=models.CharField(max_length=100)
    contacts=models.ManyToManyField(Contacts)
    is_active=models.BooleanField(default=True)



class Student(models.Model):
    def userDirectoryPath(self):
        return f'students/{self.id}/profile_image'
    user=models.OneToOneField(MainUser,primary_key=True,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to=userDirectoryPath)
    registration_number=models.CharField(max_length=20,unique=True)
    registration_date=models.DateField(max_length=20,auto_now_add=True)
    year_of_Study=models.DateField()
    branch=models.ForeignKey(School,on_delete=models.SET_NULL,null=True)
    course=models.ForeignKey(Course,on_delete=models.PROTECT)
    next_of_kin=models.ForeignKey(NextOfKin,on_delete=models.SET_NULL,null=True)
    is_active=models.BooleanField(default=True)



class Subjects(models.Model):
    subject_code=models.CharField(max_length=10)
    subject_name=models.CharField(max_length=50)
    course=models.ManyToManyField(Course)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

 
class Instructor(models.Model):
    user_id=models.OneToOneField(MainUser,primary_key=True,on_delete=models.CASCADE)
    subjects=models.ManyToManyField(Subjects)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    branch=models.ManyToManyField(School)
    next_of_kin=models.ForeignKey(NextOfKin,on_delete=models.SET_NULL,null=True)
    is_active=models.BooleanField(default=True)

    

class RoomType(models.Model):
    room_type_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


class Rooms(models.Model):
    room_code=models.CharField(max_length=10)
    room_type=models.ForeignKey(RoomType,on_delete=models.SET_NULL,null=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


class Schedule(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.PROTECT)
    subject_id=models.ForeignKey(Subjects,on_delete=models.PROTECT)
    instructor_id=models.ForeignKey(Instructor,on_delete=models.PROTECT)
    is_active=models.BooleanField(default=True)
    start_time=models.TimeField()
    duration_in_minutes=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)



    
