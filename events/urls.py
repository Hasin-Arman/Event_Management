from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'registrations', views.RegistrationViewset,basename='registration')

urlpatterns = [
    path('',include(router.urls)),
    path('events/<int:pk>/',views.SingleEventView.as_view()),
    path('events/',views.AllEventsView.as_view()),
    path('register_event/<int:id>/',views.registerView,name='register_event'),
    path('unregister/<int:id>/',views.unregister,name='unregister'),
    path('profile/',views.profile,name='profile'),
]