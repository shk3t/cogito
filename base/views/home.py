from django.shortcuts import render


def home(request):
    context = {"username": request.user.username}
    return render(request, "base/home.html", context)
