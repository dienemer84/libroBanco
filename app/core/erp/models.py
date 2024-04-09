from django.db import models
from datetime import datetime

from django.forms import model_to_dict


# Create your models here.

class Proveedor(models.Model):
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
    detalle = models.CharField(max_length=200, verbose_name='Detalle')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        db_table = 'banco'
        ordering = ['id']


class Cheque(models.Model):
    numero = models.CharField(max_length=150, verbose_name='Numero')
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name='Fecha de Ingreso')
    fecha_actualizacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Actualización')
    fecha_emision = models.DateField(default=datetime.now, verbose_name='Fecha de Emisión')
    fecha_pago = models.DateField(default=datetime.now, verbose_name='Fecha de Pago')
    fecha_vto = models.DateField(default=datetime.now, verbose_name='Fecha de Vencimiento')
    valor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.numero

    def toJSON(self):
        item = model_to_dict(self)
        item['banco'] = self.banco.nombre
        item['proveedor'] = self.proveedor.razonsocial
        item['fecha_ingreso'] = self.fecha_ingreso.strftime('%d-%m-%Y')
        item['fecha_actualizacion'] = self.fecha_actualizacion.strftime('%d-%m-%Y')
        item['fecha_emision'] = self.fecha_emision.strftime('%d-%m-%Y')
        item['fecha_pago'] = self.fecha_pago.strftime('%d-%m-%Y')
        item['fecha_vto'] = self.fecha_vto.strftime('%d-%m-%Y')
        return item

    class Meta:
        verbose_name = 'Cheque'
        verbose_name_plural = 'Cheques'
        db_table = 'cheque'
        ordering = ['id']


