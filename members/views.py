from django.shortcuts import render, redirect
from .models import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, ('Registration successful'))
            return redirect('login')
    return render(request, 'registration/register.html', {'form': form,})