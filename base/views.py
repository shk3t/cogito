from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages as flash_messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .forms import LoginForm, MessageForm, SourceForm
from base.models import Cluster, Source, Message


def home(request):
    context = {"username": request.user.username}
    return render(request, "base/home.html", context)


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
    page_type = "Login"
    context = {"form": form, "page_type": page_type}
    return render(request, "base/login-register.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


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
    page_type = "Register"
    context = {"form": form, "page_type": page_type}
    return render(request, "base/login-register.html", context)


def cluster(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)
    context = {"cluster": cluster}
    return render(request, "base/cluster.html", context)


def source_list(request):
    name_param = request.GET.get("name")
    if name_param:
        sources = Source.objects.filter(name__icontains=name_param)
    else:
        sources = Source.objects.all()
    count = sources.count()
    context = {"sources": sources, "count": count}
    return render(request, "base/source-list.html", context)


def source(request, source_id):
    source = Source.objects.get(id=source_id)
    form = MessageForm()
    source_messages = Message.objects.filter(source_id=source_id)
    context = {"source": source, "form": form, "messages": source_messages}
    return render(request, "base/source.html", context)


@login_required(login_url='login')
def create_source(request):
    form = SourceForm()
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            new_source = form.save(commit=False)
            new_source.author = request.user
            new_source.save()
            return redirect("source-list")
        flash_messages.error(request, "Source creation error")
    context = {"form": form}
    return render(request, "base/create-source.html", context)


@login_required(login_url='login')
def create_message(request, source_id):
    if request.method == "POST":
        form = MessageForm(request.POST)
        message_source = Source.objects.get(id=source_id)
        message_body = form.data.get("body")
        new_message = Message(
            user=request.user, source=message_source, body=message_body
        )
        new_message.save()
    return redirect(reverse("source", args=(message_source.id,)))


def global_chat(request):
    messages = Message.objects.all()
    context = {"messages": messages}
    return render(request, "base/global-chat.html", context)
