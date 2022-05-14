from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import Contacts, MainUser,Permissions,UserRole,Location
# Register your models here.

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)
    class Meta:
        model=MainUser
        fields=("username","first_name","last_name")
    
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords dont match")
        return password2
    
    def save(self,commit=True):
        #save the provided password in hashed format
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=MainUser
        fields = ('username', 'password','first_name','last_name','gender', 'date_of_birth', 'is_active','is_staff', 'is_admin')

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=('username','first_name','is_admin')
    list_filter=('is_admin','is_staff')
    fieldsets=(
        (None,{'fields':('username','password','first_name','last_name')}),
        ('Personal info', {'fields': ('gender', 'date_of_birth')}),
        ('Permissions',{'fields':('is_admin','is_staff','is_student')}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal=()

admin.site.unregister(Group)
admin.site.register(MainUser,UserAdmin)
models=[Permissions,UserRole,Location,Contacts]
for model in models:
    admin.site.register(model)