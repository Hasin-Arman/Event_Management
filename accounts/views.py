from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def user_register(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('profile')
    return render(request, 'register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'signin.html',{'error': 'Invalid username or password'})
    return render(request, 'signin.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('homepage')
    
