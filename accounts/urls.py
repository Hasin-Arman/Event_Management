from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.user_register,name="registerpage"),
    path('login/',views.user_login,name="loginpage"),
    path('logout/',views.user_logout,name="logoutpage"),
]