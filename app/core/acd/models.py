from django.db import models

# Create your models here.

""" class TypeUser(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'type_user'

class Vendor(models.Model):
    names = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    phone_number = models.IntegerField(max_length=10, verbose_name='Número de celular')
    email = models.CharField(max_length=50, verbose_name='Correo electrónico')
    id_type = models.ForeignKey(TypeUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vendor'

class Platform(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'platform'

class Service(models.Model):
    email_account = models.CharField(max_length=50, verbose_name='Correo cuenta')
    profile_quantity = models.CharField(max_length=50, verbose_name='Cantidad de perfiles')
    id_platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service'


class Client(models.Model):
    names = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    phone_number = models.IntegerField(max_length=10, verbose_name='Número de celular')
    email = models.CharField(max_length=50, verbose_name='Correo electrónico')

    class Meta:
        db_table = 'client'

class VendorService(models.Model):
    id_vendor = models.ForeignKey(Vendor)
    id_client = models.ForeignKey(Client)
    id_service = models.ForeignKey(Service)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        db_table = 'vendor_service' """