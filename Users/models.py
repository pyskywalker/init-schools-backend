from tkinter import CASCADE
from urllib.request import CacheFTPHandler
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager

from phonenumber_field.modelfields import PhoneNumberField

import datetime

class Location(models.Model):
    village=models.CharField(max_length=100,null=True,blank=True)
    ward=models.CharField(max_length=100,null=True,blank=True)
    district=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100)
    region=models.CharField(max_length=100)
    country=models.CharField(max_length=100,default="United Republic Of Tanzania",null=True)
    def __str__(self):
        return f"{self.city} {self.region} {self.country}"

class Contacts(models.Model):
    email=models.EmailField(null=True)
    phone=PhoneNumberField(null=True)
    def __str__(self):
        return f"{self.email}"

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
class Permissions(models.Model):
    permission_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.permission_name}"
class UserRole(models.Model):
    role_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    permission=models.ManyToManyField(Permissions,related_name="rolePermission")
    def __str__(self):
        return f"{self.role_name}"

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
    gender=models.CharField(max_length=1,choices=genderChoices,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    is_staff=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_instructor=models.BooleanField(default=False)
    contacts=models.ForeignKey(Contacts,on_delete=models.SET_NULL,null=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    nationality=models.CharField(default="United Republic of Tanzania",max_length=100,null=True )
    user_roles=models.ManyToManyField(UserRole)
    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.username}'




    
    

