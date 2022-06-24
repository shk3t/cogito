from django.shortcuts import render, redirect
from django.contrib import messages as flash_messages
from django.contrib.auth.models import User

from base.models import Message


def get_user_info(request, user_id):
    user = User.objects.get(id=user_id)
    user_messages = Message.objects.filter(user_id=user_id)
    context = {"user": user, "messages": user_messages}
    return render(request, "base/profile.html", context)
