# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    administratorid = models.AutoField(db_column='AdministratorID', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=255)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=25)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Administrator'


class Dowodos(models.Model):
    dowodid = models.AutoField(db_column='DowodID', primary_key=True)  # Field name made lowercase.
    uzytkownikid = models.ForeignKey('Uzytkownik', models.DO_NOTHING, db_column='UzytkownikID')  # Field name made lowercase.
    seria = models.CharField(db_column='Seria', unique=True, max_length=9)  # Field name made lowercase.
    pesel = models.CharField(db_column='PESEL', unique=True, max_length=11)  # Field name made lowercase.
    adres = models.CharField(db_column='Adres', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DowodOs'


class Liga(models.Model):
    ligaid = models.AutoField(db_column='LigaID', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', unique=True, max_length=255)  # Field name made lowercase.
    opis = models.CharField(db_column='Opis', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Liga'


class Turniej(models.Model):
    turniejid = models.AutoField(db_column='TurniejID', primary_key=True)  # Field name made lowercase.
    ligaid = models.ForeignKey(Liga, models.DO_NOTHING, db_column='LigaID', blank=True, null=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=255)  # Field name made lowercase.
    datastart = models.DateField(db_column='DataStart')  # Field name made lowercase.
    datazakonczenia = models.DateField(db_column='DataZakonczenia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Turniej'


class Uczestnik(models.Model):
    uczestnikid = models.AutoField(db_column='UczestnikID', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=255)  # Field name made lowercase.
    kraj = models.CharField(db_column='Kraj', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Uczestnik'


class Uzytkownik(models.Model):
    uzytkownikid = models.AutoField(db_column='UzytkownikID', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=255)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=255)  # Field name made lowercase.
    wiek = models.IntegerField(db_column='Wiek')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=25)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=25)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='Saldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adreskontabankowego = models.CharField(db_column='AdresKontaBankowego', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Uzytkownik'


class Wydarzenie(models.Model):
    wydarzenieid = models.AutoField(db_column='WydarzenieID', primary_key=True)  # Field name made lowercase.
    turniejid = models.ForeignKey(Turniej, models.DO_NOTHING, db_column='TurniejID', blank=True, null=True)  # Field name made lowercase.
    administratorid = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='AdministratorID', blank=True, null=True)  # Field name made lowercase.
    miejsce = models.CharField(db_column='Miejsce', max_length=255)  # Field name made lowercase.
    datastartu = models.DateTimeField(db_column='DataStartu')  # Field name made lowercase.
    datazakonczenia = models.DateTimeField(db_column='DataZakonczenia')  # Field name made lowercase.
    gospodarzid = models.ForeignKey(Uczestnik, models.DO_NOTHING, db_column='GospodarzID', related_name='gospodarz')  # Field name made lowercase.
    goscid = models.ForeignKey(Uczestnik, models.DO_NOTHING, db_column='GoscID', related_name='gosc')  # Field name made lowercase.
    kursgospodarz = models.DecimalField(db_column='KursGospodarz', max_digits=6, decimal_places=3)  # Field name made lowercase.
    kursgosc = models.DecimalField(db_column='KursGosc', max_digits=6, decimal_places=3)  # Field name made lowercase.
    wynik = models.CharField(db_column='Wynik', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Wydarzenie'


class Zaklad(models.Model):
    zakladid = models.AutoField(db_column='ZakladID', primary_key=True)  # Field name made lowercase.
    uzytkownikid = models.ForeignKey(Uzytkownik, models.DO_NOTHING, db_column='UzytkownikID', blank=True, null=True)  # Field name made lowercase.
    wydarzenieid = models.ForeignKey(Wydarzenie, models.DO_NOTHING, db_column='WydarzenieID', blank=True, null=True)  # Field name made lowercase.
    wybranykurs = models.DecimalField(db_column='WybranyKurs', max_digits=6, decimal_places=3)  # Field name made lowercase.
    datazakladu = models.DateTimeField(db_column='DataZakladu')  # Field name made lowercase.
    ileobstawione = models.DecimalField(db_column='IleObstawione', max_digits=19, decimal_places=4)  # Field name made lowercase.
    mozliwawygrana = models.DecimalField(db_column='MozliwaWygrana', max_digits=26, decimal_places=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zaklad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
