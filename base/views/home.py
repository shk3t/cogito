from django.shortcuts import redirect, render


def blank(request):
    return redirect("home")

def home(request):
    context = {"username": request.user.username}
    return render(request, "base/home.html", context)
