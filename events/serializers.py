from rest_framework import serializers
from .models import event,event_registration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=event
        fields="__all__"
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=event_registration
        fields="__all__"