from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token as AuthToken
from django.contrib.sessions.models import Session



class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)


class Token(AuthToken):
    key = models.CharField("Key", max_length=40, db_index=True, unique=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="auth_token",
        on_delete=models.CASCADE,
        verbose_name="MainUser",
    )

