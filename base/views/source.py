from django.shortcuts import render, redirect
from django.contrib import messages as flash_messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from base.models import Source, Message
from base.forms import MessageForm, SourceForm


@login_required(login_url="login")
def create_source(request):
    form = SourceForm()
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            new_source = form.save(commit=False)
            new_source.user = request.user
            new_source.save()
            return redirect("source-list")
        flash_messages.error(request, "Source creation error")
    context = {"form": form}
    return render(request, "base/source-form.html", context)


@login_required(login_url="login")
def update_source(request, source_id):
    source = Source.objects.get(id=source_id)
    if request.method == "POST":
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return redirect("source-list")
        flash_messages.error(request, "Source updation error")
    form = SourceForm(instance=source)
    context = {"form": form}
    return render(request, "base/source-form.html", context)


def get_source(request, source_id):
    source = Source.objects.get(id=source_id)
    form = MessageForm()
    source_messages = Message.objects.filter(source_id=source_id)
    context = {"source": source, "form": form, "messages": source_messages}
    return render(request, "base/source.html", context)


def list_sources(request):
    name_param = request.GET.get("name")
    if name_param:
        sources = Source.objects.filter(name__icontains=name_param)
    else:
        sources = Source.objects.all()
    if User.is_authenticated:
        user_sources = sources.filter(user_id=request.user.id)
    context = {"sources": sources, "user_sources": user_sources}
    return render(request, "base/source-list.html", context)


@login_required(login_url="login")
def delete_source(request, source_id):
    source = Source.objects.get(id=source_id)
    source.delete()
    # TODO make it POST
    # TODO add confirmation form
    return redirect("source-list")
