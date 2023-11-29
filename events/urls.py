from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'events', views.EventViewset,basename='event')
router.register(r'registrations', views.RegistrationViewset,basename='registration')

urlpatterns = [
    path('api/',include(router.urls)),
    path('register_event/<int:id>/',views.registerView,name='register_event'),
    path('unregister/<int:id>/',views.unregister,name='unregister'),
    path('profile/',views.profile,name='profile'),
]