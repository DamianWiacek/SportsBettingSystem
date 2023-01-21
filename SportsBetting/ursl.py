from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('Wydarzenia/',views.Wydarzenia,name = 'Wydarzenia'),
    path('Zaklady/<str:uczestnik>/<str:data>/<str:kurs>/<int:wydarzenieid>',views.Zaklady,name = 'Zaklady'),
    path('Rejestracja/',views.Rejestracja,name = 'Rejestracja'),
    path('Login/',views.Login, name = "login" ),
    path('Wyloguj/',views.Wyloguj, name = "Wyloguj" ),
    path('ZapiszZaklad/',views.ZapiszZaklad, name = "ZapiszZaklad" ),
    path('AdminPanel/', views.AdminPanel, name = "AdminPanel"),
    path('AdminLogin/', views.AdminLogin, name = "AdminLogin"),
    path('AdminWyloguj/', views.AdminWyloguj, name = "AdminWyloguj"),
    path('DodajLige/',views.DodajLige,name='DodajLige'),
    path('DodajTurniej/',views.DodajTurniej,name='DodajTurniej'),
    path('DodajWydarzenie/',views.DodajWydarzenie,name='DodajWydarzenie'),
]