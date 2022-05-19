from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from base.models import Source, Message
from base.forms import MessageForm


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


def get_all_messages(request, page=1):
    messages = Message.objects.all()
    message_paginator = Paginator(messages, 10)
    message_page = message_paginator.page(page)
    context = {"messages": messages, "page": message_page}
    return render(request, "base/global-chat.html", context)
