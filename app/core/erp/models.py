from django.db import models
from datetime import datetime


# Create your models here.

class Employable(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    fecha_ingreso = models.DateField(default=datetime.now, verbose_name='Fecha de Ingreso')
    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización')
    edad = models.PositiveIntegerField(default=0)
    genero = models.CharField(max_length=50)
    sueldo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d', null=True, blank=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']


class Proved(models.Model):
    razonsocial = models.CharField(max_length=200, verbose_name='Proveedor')
    cuit = models.CharField(max_length=14, verbose_name='CUIT')

    def __str__(self):
        return self.razonsocial

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['id']


class Banco(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        db_table = 'banco'
        ordering = ['id']

class Cheque(models.Model):
    numero = models.CharField(max_length=150, verbose_name='Nombre')
    fecha_ingreso = models.DateField(default=datetime.now, verbose_name='Fecha de Ingreso')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización')
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Emisión')
    fecha_pago = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pago')
    fecha_vto = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Vencimiento')
    valor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True)
    pagado = models.BooleanField(default=True)
    proveedor = models.ForeignKey(Proved, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'Cheque'
        verbose_name_plural = 'Cheques'
        db_table = 'cheque'
        ordering = ['id']





