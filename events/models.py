from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class event(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=100)
    registered_user=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class event_registration(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    events=models.ForeignKey(event,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=11)
    email=models.EmailField()
    university=models.CharField(max_length=50)
    
    def __str__(self):
        return self.events.title
    