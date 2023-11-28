
from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="homepage"),
    path('',include('accounts.urls')),
    path('',include('events.urls'))
]
