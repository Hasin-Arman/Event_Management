from django.urls import path
from . import views

urlpatterns = [
    path('register_event/<int:id>/',views.registerView,name='register_event'),
    path('unregister/<int:id>/',views.unregister,name='unregister'),
    path('profile/',views.profile,name='profile'),
]