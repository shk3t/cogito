from django.shortcuts import render, redirect
from django.contrib import messages as flash_messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from base.models import Source, Message, Cluster
from base.forms import MessageForm, SourceForm


@login_required(login_url="login")
def create_source(request):
    if request.method == "POST":
        form = SourceForm(request.POST, request.FILES)
        if form.is_valid():
            new_source = Source(
                name=form.cleaned_data["name"],
                user=request.user,
                description=form.cleaned_data["description"],
                content=form.cleaned_data["content"],
                cluster=form.cleaned_data["cluster"],
            )
            new_source.save()
            return redirect("source-list")
        flash_messages.error(request, "Source creation error")

    form = SourceForm()
    context = {"form": form}
    return render(request, "base/source-form.html", context)


@login_required(login_url="login")
def update_source(request, source_id):
    old_source = Source.objects.get(id=source_id)

    if request.method == "POST":
        form = SourceForm(request.POST, request.FILES)
        if form.is_valid():
            if form.files:
                new_content = form.cleaned_data["content"]
                old_source.content.delete()
            elif form.data.get("content-clear"):
                new_content = None
                old_source.content.delete()
            else:
                new_content = old_source.content
            updated_source = Source(
                id=source_id,
                name=form.cleaned_data["name"],
                user=User.objects.get(id=old_source.user_id),
                description=form.cleaned_data["description"],
                content=new_content,
                cluster=form.cleaned_data["cluster"],
            )
            updated_source.save()
            return redirect("source-list")
        flash_messages.error(request, "Source updation error")

    source_dict = {
        "name": old_source.name,
        "description": old_source.description,
        "content": old_source.content,
        "cluster": old_source.cluster,
    }
    form = SourceForm(initial=source_dict)
    context = {"form": form}
    return render(request, "base/source-form.html", context)


def get_source(request, source_id):
    source = Source.objects.get(id=source_id)
    form = MessageForm()
    source_messages = Message.objects.filter(source_id=source_id)
    context = {"source": source, "form": form, "messages": source_messages}
    return render(request, "base/source.html", context)


def list_sources(request):
    cluster_id = request.GET.get("cluster_id")
    if cluster_id:
        try:
            current_cluster = Cluster.objects.get(id=cluster_id)
        except Cluster.DoesNotExist:
            return redirect("source-list")
        clusters = Cluster.objects.filter(parent_cluster=cluster_id)
        sources = Source.objects.filter(cluster_id=cluster_id)
    else:
        current_cluster = Cluster(name="Global")
        clusters = Cluster.objects.filter(parent_cluster__isnull=True)
        sources = Source.objects.all()

    name_param = request.GET.get("name")
    if name_param:
        sources = sources.filter(name__icontains=name_param)

    if User.is_authenticated:
        user_sources = Source.objects.filter(user_id=request.user.id)

    context = {
        "sources": sources,
        "user_sources": user_sources,
        "current_cluster": current_cluster,
        "clusters": clusters,
    }
    return render(request, "base/source-list.html", context)


@login_required(login_url="login")
def delete_source(request, source_id):
    source = Source.objects.get(id=source_id)
    source.delete()
    # TODO make it POST
    # TODO add confirmation form
    return redirect("source-list")
