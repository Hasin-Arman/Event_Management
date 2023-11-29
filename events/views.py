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
            form.instance.user =request.user
            get_event.registered_user+=1
            get_event.save()
            form.save()
            return redirect('homepage')
    else:
        form = registrationForm()
    return render(request, 'register_event.html', {'form': form})

@login_required(login_url = '/login/') 
def profile(request):
    registered = event_registration.objects.filter(user=request.user)
    return render(request, 'profile.html',{'registers':registered})

def unregister(request,id):
    get_event=event.objects.get(id=id)
    get_event.registered_user-=1
    get_registration=event_registration.objects.get(events=get_event,user=request.user)
    if get_registration.user == request.user:
        get_registration.user = None
        get_registration.save()
    get_event.save()
    return redirect('homepage')
    # events=event_registration.objects.exclude(events=get_event)
    # return render(request, 'profile.html',{'registers':events})
    