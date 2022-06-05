from django.contrib import admin
from .models import *
# Register your models here.
models=[Student,Schedule,Instructor,NextOfKin,Course,Subjects,School,RoomType,Rooms,Assignments,StudentsAssignments,CourseItems,CourseOutline,CourseItemType,Specializations]

for model in models:
    admin.site.register(model)