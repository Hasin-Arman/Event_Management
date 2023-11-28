from django.shortcuts import render
from events.models import event,event_registration
def home(request):
    events =event.objects.all()
    return render(request, 'index.html',{'events':events})