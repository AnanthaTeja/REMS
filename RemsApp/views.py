from django.shortcuts import render, redirect
from .models import User
from .forms import NwForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "html/home.html")


def about(request):
    return render(request, "html/about.html")


def contact(request):
    return render(request, "html/contact.html")


def register(request):
    if request.method == "POST":
        f = NwForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, "User Created Successfully")
            return redirect("/lgn")
    else:
        f = NwForm()
    return render(request, "html/register.html")
