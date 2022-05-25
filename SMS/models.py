from http.client import PROCESSING
from platform import mac_ver
from django.db import models
from Users.models import MainUser,Location,Contacts
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.


class School(models.Model):
    branch_name=models.CharField(max_length=100)
    location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    principal=models.ForeignKey(MainUser,on_delete=models.SET_NULL,null=True)
    contacts=models.ForeignKey(Contacts,on_delete=models.SET_NULL,null=True)
    is_active=models.BooleanField(default=True)


class Subjects(models.Model):
    subject_code=models.CharField(max_length=10)
    subject_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
       return f"{self.subject_code}: {self.subject_name}"

class Course(models.Model):
    course_code=models.CharField(max_length=10)
    course_name=models.CharField(max_length=100)
    school_year=models.IntegerField()
    subjects=models.ManyToManyField(Subjects,related_name="course_subjects")
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.course_code} : {self.course_name}"

class NextOfKin(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,null=True,blank=True)
    relationship=models.CharField(max_length=100)
    contacts=models.ManyToManyField(Contacts)
    is_active=models.BooleanField(default=True)

def yearpublished(date):
        return date.pub_date.strftime('%Y')
def f(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return '{}.{}'.format(instance.pk, ext)
    else:
        pass

class Student(models.Model):
    def userDirectoryPath(instance,filename):
        ext = filename.split('.')[-1]
        date_string=str(timezone.now())
        st=date_string.replace(r'/','-').replace(r" ","-").replace(r":","-").replace(r"+","-")
        st=instance.registration_number

        st=st+"."+ext
        return f'students/profile_image/{st}'
    user=models.OneToOneField(MainUser,primary_key=True,on_delete=models.CASCADE)
    registration_number=models.CharField(max_length=20,unique=True)
    
    profile_image=models.ImageField(upload_to=userDirectoryPath)
    registration_date=models.DateField(max_length=20,auto_now_add=True)
    year_of_Study=models.DateField()
    branch=models.ForeignKey(School,on_delete=models.SET_NULL,null=True)
    course=models.ForeignKey(Course,on_delete=models.PROTECT)
    next_of_kin=models.ForeignKey(NextOfKin,on_delete=models.SET_NULL,null=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Instructor(models.Model):
    user_id=models.OneToOneField(MainUser,primary_key=True,on_delete=models.CASCADE)
    subjects=models.ManyToManyField(Subjects)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    branch=models.ManyToManyField(School)
    next_of_kin=models.ForeignKey(NextOfKin,on_delete=models.SET_NULL,null=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
       return f"{self.user_id.username}: {self.user_id.first_name} {self.user_id.last_name}"

    

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



    
class Assignments(models.Model):
    assignment_name=models.CharField(max_length=200)
    assingment_file=models.FileField()
    subject=models.ForeignKey(Subjects,on_delete=models.PROTECT)
    assigned_by=models.ForeignKey(Instructor,on_delete=models.PROTECT)
    due_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    created_by=models.ForeignKey(MainUser,on_delete=models.PROTECT)
    def save(self,*args,**kwargs):
       super(Assignments, self).save(*args, **kwargs)
       students=Student.objects.filter(course__subjects=self.subject)
       for student in students:
          student_assignment= StudentsAssignments.objects.create(student=student,assignment=self)
          student_assignment.save()


class StudentsAssignments(models.Model):
    assignment=models.ForeignKey(Assignments,on_delete=models.PROTECT)
    student=models.ForeignKey(Student,on_delete=models.PROTECT)
    assignment_done=models.FileField(null=True)
    is_completed=models.BooleanField(default=False)
    submitted_on=models.DateTimeField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    

class CourseItemType(models.Model):
    type_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
class CourseOutline(models.Model):
    subject=models.ForeignKey(Subjects,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    

class CourseItems(models.Model):
    item_name=models.CharField(max_length=100)
    course_outline=models.ForeignKey(CourseOutline,on_delete=models.PROTECT)
    created_by=models.ForeignKey(MainUser,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    




