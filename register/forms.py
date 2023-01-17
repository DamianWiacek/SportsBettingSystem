from django.forms import ModelForm, forms, PasswordInput, EmailInput
from models import Uzytkownik


class RegisterForm(ModelForm):
    Imie = forms.CharField(max_length=100)
    Nazwisko = forms.CharField(max_length=100)
    Username = forms.CharField(max_length=100)
    Passwd = forms.CharField(widget=PasswordInput)
    Email = forms.CharField(widget=EmailInput)


    class Meta:
        model = Uzytkownik
        fields = ["Imie","Nazwisko","Wiek","Username","Passwd","Email","Saldo","AdresKontaBankowego","Seria","Pesel","Adres"]