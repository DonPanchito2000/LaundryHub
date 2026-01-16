from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import LoginForm

def home(request):
    return render(request, 'account/home.htm')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username = email, password=password)

            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('home')
            
            messages.error(request,'Invalid email or password')
    else:
        form =LoginForm()

    return render(request, 'account/login.htm' , {'form':form})


def logout_view(request):
    logout(request)
    return redirect('login') 