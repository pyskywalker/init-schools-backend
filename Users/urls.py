from .views import *
from django.urls import path
urlpatterns = [
    path('userlist',UserList.as_view(),name="users"),
    path('user-role-list',UserRolesAPI.as_view(),name="user-roles"),
    ]
