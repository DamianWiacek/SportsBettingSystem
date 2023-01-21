import datetime
import decimal

from django.db.models import Count,Sum
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render, redirect
from dateutil import parser
from register.forms import RegisterForm,DowodForm
from .models import Wydarzenie,Uzytkownik,Zaklad,Dowodos,Administrator,Liga,Turniej,Uczestnik
import  pandas as pd

# Create your views here.



def home(request):
    zaklady = Zaklad.objects.filter(uzytkownikid=request.session['LoggedUser'])
    users = Uzytkownik.objects.filter(uzytkownikid=request.session['LoggedUser'])
    user = users.first()
    return render(request, 'SportsBetting/Home.html', {"user" : user, "zaklady":zaklady})


def Wydarzenia(request):
    wydarzenia = Wydarzenie.objects.filter(datastartu__gt = datetime.datetime.now())
    return render(request, 'SportsBetting/Wydarzenia.html', {'Wydarzenia':wydarzenia,"user":request.session['LoggedUser']})


def Zaklady(request,uczestnik,data, kurs,wydarzenieid):
    if request.method == 'POST':
        ZakladForm = { "data" : parser.parse(data),
                       "kurs": float(kurs),
                       "user":request.session['LoggedUser'],
                       "uczestnik":uczestnik,
                       "ileObstawione":int(request.POST.get("wysokoscZakladu")),
                       "wydarzenieid":wydarzenieid,
                       "wysokoscZakladu":round((int(request.POST.get("wysokoscZakladu")))*float(kurs),2)}

        return render(request,'SportsBetting/PotwierdzZaklad.html', ZakladForm)

    return render(request, 'SportsBetting/Zaklady.html', {"uczestnik": uczestnik,
                                                          "data" : parser.parse(data),
                                                          "kurs": float(kurs),
                                                          "user":request.session['LoggedUser']})


def Rejestracja(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
             user = form.save()
             adres = request.POST.get('adres')
             seria = request.POST.get('seria')
             pesel = request.POST.get('pesel')
             dowod = Dowodos.objects.create(uzytkownikid = user, adres=adres,seria=seria,pesel=pesel)
             dowod.save()

        return redirect("/")
    else:
        form = RegisterForm()
        form1 = DowodForm()

    return render(request, "SportsBetting/Rejestracja.html", {"form": form, "form1" : form1})

def Login(request):
    if request.method=="POST":
        usname = request.POST.get('username')
        password = request.POST.get('passwd')

        user = Uzytkownik.objects.get(passwd=password, username=usname)

        if user is not None:
            request.session['LoggedUser'] = user.uzytkownikid
            return redirect('/')
        else:

            return redirect('Rejestracja')

    return render(request,"SportsBetting/Login.html",{})

def Wyloguj(request):

    request.session['LoggedUser'] = None
    return redirect('/')
def ZapiszZaklad(request):
    if request.method == "POST":

        uzytkownik = request.POST["uzytkownikid"]
        wydarzenie = request.POST["wydarzenieid"]
        kurs = request.POST["wybranykurs"]
        data = parser.parse(request.POST["datazakladu"]).isoformat()
        obstawione= request.POST["ileobstawione"]
        mozliwawygrana = request.POST["mozliwawygrana"]

        nowyZaklad = Zaklad.objects.create(wybranykurs=kurs,
                                           uzytkownikid_id=uzytkownik,
                                           datazakladu=data,
                                           wydarzenieid_id=wydarzenie,
                                           ileobstawione=obstawione,
                                           mozliwawygrana=mozliwawygrana)

        nowyZaklad.save()
        user = Uzytkownik.objects.get(uzytkownikid=uzytkownik)
        user.saldo -= decimal.Decimal(obstawione)
        user.save()
        return redirect("/")


def AdminPanel(request):
    najpopularniejszeLigi = Wydarzenie.objects.select_related('turniejid').select_related('turniejid__ligaid').values('turniejid__ligaid__nazwa').annotate(Liczba_Wydarzen = Count('wydarzenieid')).order_by('-Liczba_Wydarzen')
    najwiecejobstawiajacy = Zaklad.objects.select_related('uzytkownikid').values('uzytkownikid__username').annotate(Suma_zakladow = Sum('ileobstawione')).order_by('-Suma_zakladow')
    return render(request,'SportsBetting/AdminPanel.html',{"admin" : request.session['Admin'], 'ligi':najpopularniejszeLigi, 'uzalezniency':najwiecejobstawiajacy})


def AdminLogin(request):
    if request.method == "POST":
        usname = request.POST.get('username')
        password = request.POST.get('passwd')

        admin = Administrator.objects.get(passwd=password, username=usname)

        if admin is not None:
            request.session['Admin'] = admin.administratorid
            return redirect('/AdminPanel')

    return render(request, "SportsBetting/AdminLogin.html", {})

def AdminWyloguj(request):

    request.session['Admin'] = None
    return redirect('/AdminLogin')

def DodajLige(request):
    if request.method == 'POST':
        nazwa = request.POST['nazwa']
        opis = request.POST['opis']
        nowaLiga = Liga(nazwa=nazwa, opis= opis)
        nowaLiga.save()
    return render(request,'SportsBetting/DodajLige.html', {"admin" : request.session['Admin']})

def DodajTurniej(request):
    if request.method == 'POST':
        liga = request.POST['liga']
        nazwa = request.POST['nazwa']
        datastart = parser.parse(request.POST['datastart'])
        datakoniec = parser.parse(request.POST['datakoniec'])
        nowyTurniej = Turniej(ligaid_id=liga, nazwa=nazwa,datastart=datastart,datazakonczenia=datakoniec)
        nowyTurniej.save()
    return render(request,'SportsBetting/DodajTurniej.html', {"admin" : request.session['Admin']})

def DodajWydarzenie(request):
    if request.method == 'POST':
        turniejid = request.POST['turniejid']
        miejsce = request.POST['miejsce']
        datastart = parser.parse(request.POST['datastart'])
        datakoniec = parser.parse(request.POST['datakoniec'])

        gospodarznazwa = request.POST['gospodarznazwa']
        gospodarzkraj = request.POST['gospodarzkraj']
        kursgospodarz = request.POST['kursgospodarz']

        goscnazwa = request.POST['goscnazwa']
        gosckraj = request.POST['gosckraj']
        kursgosc = request.POST['kursgosc']

        if gospodarznazwa == goscnazwa:
            raise SuspiciousOperation("Gość i gospodarz to nie moga być ci sami uczestnicy")
        else:
            try:
                gosc = Uczestnik.objects.get(nazwa=goscnazwa)
            except Uczestnik.DoesNotExist:
                gosc = Uczestnik.objects.create(nazwa=goscnazwa, kraj=gosckraj)
                gosc.save()
            try:
                gospodarz = Uczestnik.objects.get(nazwa=gospodarznazwa)
            except Uczestnik.DoesNotExist:
                gospodarz = Uczestnik.objects.create(nazwa=gospodarznazwa, kraj=gospodarzkraj)
                gospodarz.save()

        wydarzenie = Wydarzenie.objects.create(turniejid_id=turniejid,
                                               miejsce=miejsce,
                                               datastartu=datastart,
                                               datazakonczenia=datakoniec,
                                               administratorid_id=request.session['Admin'],
                                               gospodarzid_id=gospodarz.pk,
                                               kursgospodarz=kursgospodarz,
                                               goscid_id=gosc.pk,
                                               kursgosc=kursgosc)

        wydarzenie.save()
    return render(request,'SportsBetting/DodajWydarzenie.html',{"admin" : request.session['Admin']})