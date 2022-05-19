from django.shortcuts import render, redirect
from django.contrib import messages as flash_messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from base.forms import LoginForm


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect("login")
        flash_messages.error(request, "Registration error")
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "base/auth.html", context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username").lower()
            password = form.cleaned_data.get("password")
            try:
                User.objects.get(username=username)  # check if exists
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("home")
            except:
                pass
        flash_messages.error(request, "Login error")
    form = LoginForm()
    context = {"form": form}
    return render(request, "base/auth.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")
