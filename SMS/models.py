from django.db import models
from Users.models import MainUser

# Create your models here.
class Student(models.Model):
    def userDirectoryPath(self):
        return f'students/{self.id}/profile_image'
    user_id=models.OneToOneField(MainUser)
    profile_image=models.ImageField(upload_to=userDirectoryPath)
    
