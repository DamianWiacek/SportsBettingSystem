from django.shortcuts import render, redirect
from django.http import HttpResponse

from register.forms import RegisterForm
from .models import Wydarzenie, Zaklad


# Create your views here.


def home(response):
    return render(response, 'SportsBetting/Home.html', {})


def Wydarzenia(request):
    args = {}
    args['Wydarzenia'] = Wydarzenie.objects.all()
    return render(request, 'SportsBetting/Wydarzenia.html', args)


def Zaklady(response, kurs):
    return render(response, 'SportsBetting/Zaklady.html', {"kurs": float(kurs)})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
