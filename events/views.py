from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import registrationForm
from django.contrib.auth.decorators import login_required
from .models import event,event_registration
# Create your views here.

@login_required(login_url = '/login/')
def registerView(request,id):
    get_event=event.objects.get(id=id)
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.instance.events = get_event
            get_event.registered_user+=1
            get_event.users=request.user
            get_event.save()
            form.save()
            return redirect('homepage')
    else:
        form = registrationForm()
    return render(request, 'register_event.html', {'form': form})
    
def profile(request):
    registered = event.objects.filter(users=request.user)
    return render(request, 'profile.html',{'events':registered})

def unregister(request,id):
    get_event=event.objects.get(id=id)
    get_event.registered_user-=1
    if get_event.users == request.user:
        get_event.users=None
    get_event.save()
    events=event.objects.exclude(id=id).filter(users=request.user)
    return render(request, 'profile.html',{'events':events})
    