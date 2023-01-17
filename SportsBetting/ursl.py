from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('Wydarzenia/',views.Wydarzenia,name = 'Wydarzenia'),
    path('Zaklady/<str:kurs>/',views.Zaklady,name = 'Zaklady'),
    path('Rejestracja/<str:kurs>/',views.Rejestracja,name = 'Rejestracja'),

]