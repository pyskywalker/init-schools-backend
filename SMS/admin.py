from django.contrib import admin
from .models import *
# Register your models here.
models=[Student,Schedule,Instructor,NextOfKin,Course,Subjects,School,RoomType,Rooms]

for model in models:
    admin.site.register(model)