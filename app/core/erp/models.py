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
        ordering = ['razonsocial']


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
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    fecha_emision = models.DateField(default=datetime.now, verbose_name='Fecha de Emisión')
    fecha_pago = models.DateField(default=datetime.now, verbose_name='Fecha de Pago')
    numero = models.CharField(max_length=150, verbose_name='Numero')
    op = models.CharField(max_length=150, verbose_name='OP')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    comprobantes = models.CharField(max_length=150, verbose_name='Comprobantes')
    valor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    fecha_vto = models.DateField(default=datetime.now, verbose_name='Fecha de Vencimiento')
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name='Fecha de Ingreso')
    fecha_actualizacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Actualización')
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.numero

    def toJSON(self):
        item = model_to_dict(self)
        item['banco_id'] = self.banco.id
        item['banco_nombre'] = self.banco.nombre
        item['proveedor_id'] = self.proveedor.id
        item['proveedor_nombre'] = self.proveedor.nombre
        return item

    class Meta:
        verbose_name = 'Cheque'
        verbose_name_plural = 'Cheques'
        db_table = 'cheque'
        ordering = ['id']


