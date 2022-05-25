from django.urls import path
from .views import LoginAPI,LoginCustom, SingleUser
urlpatterns = [
    path('login/',LoginAPI.as_view(),name="login"),
    path('login-test/',LoginCustom.as_view(),name="login-test"),
    path('user/',SingleUser.as_view(),name="user-test"),
]
