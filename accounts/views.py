from django.shortcuts import render, redirect
from django.contrib import messages, auth
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login as kishore, authenticate, logout


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 != password2:
            messages.error(request, 'Passwords Doesn\'t match')
            return render(request, 'register.html')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email)
            user.save()
            return redirect("login")
        return render(request, 'register.html')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            kishore(request, user)
            return redirect('/', {
                'key': user.id
            })
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
