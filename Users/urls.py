from .views import *
from django.urls import path
urlpatterns = [
    path('userlist',UserList.as_view(),name="users"),
    path('login/',LoginAPI.as_view(),name="login")

]
