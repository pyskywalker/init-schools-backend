from django.contrib import admin
from .models import UserSession,Token
# Register your models here.
models=[UserSession,Token]
for model in models:
    admin.site.register(model)