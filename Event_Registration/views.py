from django.shortcuts import render
from events.models import event,event_registration
from django.db.models import Q
def home(request):
    search=request.GET.get('search')
    if search:
        events=event.objects.filter(Q(title__icontains=search) | Q(location__icontains=search))
    else:
        events =event.objects.all()
    return render(request, 'index.html',{'events':events})