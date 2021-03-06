from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

from main.forms import SignUpForm


def home(request):
    return render(request, 'main/home.html')


def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:  # if user create
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('login')
