from django.forms import ModelForm, PasswordInput, EmailInput
from django import forms
from SportsBetting.models import Uzytkownik, Zaklad,Dowodos


class RegisterForm(ModelForm):
    saldo = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Uzytkownik
        fields = ["imie","nazwisko","wiek","username","passwd","email","adreskontabankowego","saldo"]

class DowodForm(ModelForm):
    uzytkownikid = forms.CharField(widget = forms.HiddenInput())
    class Meta:
        model = Dowodos
        fields = ["seria","pesel","adres","uzytkownikid"]

class ZakladForm(ModelForm):

    class Meta:
        model = Zaklad
        exclude = ('mozliwawygrana', )
        fields = ["uzytkownikid", "wydarzenieid", "wybranykurs", "datazakladu", "ileobstawione"]