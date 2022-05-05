from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
        def create_user(self,username,first_name,last_name,password=None):
            if not username:
                raise ValueError('User must have a username')
            user = self.model(username=username, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save(using=self._db)
            return user
        
        def create_superuser(self,username,first_name,last_name,password=None):
            user=self.create_user(username,first_name,last_name,password)
            # user=self.create_user(username,first_name=first_name,last_name=last_name,password=password)
            
            user.is_admin=True
            user.is_staff=True
            user.is_superuser=True
            user.save(using=self._db)
            return user

class UserRole(models.Model):
    role_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
class Permissions(models.Model):
    permission_name=models.CharField(max_length=200)
    role=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


class MainUser(AbstractUser,PermissionsMixin):
    def designation(self):
        if self.is_staff:
            return "Employee"
        elif self.is_student:
            return "Student"
        return "Undefined"
    genderChoices=[("F", 'Female'),
        ("M", 'Male'),
        ("O", 'Other'),]
    username=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=1,choices=genderChoices,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    user_roles=models.ManyToManyField(UserRole,null=True)
    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    class Meta:
         
        permissions = (
            ("can_go_in_non_ac_bus", "To provide non-AC Bus facility"),
            ("can_go_in_ac_bus", "To provide AC-Bus facility"),
            ("can_stay_ac-room", "To provide staying at AC room"),
            ("can_not_stay_ac-room", "To provide staying at Non-AC room"),
            ("can_go_dehradoon", "Trip to Dehradoon"),
            ("can_go_mussoorie", "Trip to Mussoorie"),
            ("can_go_haridwaar", "Trip to Haridwaar"),
            ("can_go_rishikesh", "Trip to Rishikesh"),)

    def __str__(self):
        return f'{self.username}'




    
    
            

