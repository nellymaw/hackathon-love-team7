<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect
from django.contrib.auth import logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def landing(request):
    """ docstring """
    return render(request, 'home/landing.html')

def sign_up(request):
    """ docstring """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'home/sign-up.html', {'form': form})

def logout_view(request):
    """ docstring """
    logout(request)
    messages.info(request, f'Logged out!')
    return redirect('landing-home')

>>>>>>> b691327385ea3e73dc1e1a867a4a2d4e06cf7f1e
