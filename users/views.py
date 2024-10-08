from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Users
from django.contrib.auth.decorators import login_required

def CreateUser(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = Users.objects.create_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'], 
                phone=form.cleaned_data['phone']
            )
            
            return redirect('login')  
    return render(request, 'users/cadastro.html', {'form': form}) 

def ValidateUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    
    form = RegistrationForm() 
    return render(request, 'users/login.html', {'form': form})

@login_required
def MainPage(request):
    return render(request, 'users/auth.html')
