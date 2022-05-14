from django.urls import path
from .views import LoginAPI,LoginCustom
urlpatterns = [
    path('login/',LoginAPI.as_view(),name="login"),
    path('login-test/',LoginCustom.as_view(),name="login-test"),
]
