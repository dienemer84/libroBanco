# Generated by Django 4.2.1 on 2023-06-01 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=150, verbose_name='Nombre')),
                ('banco', models.CharField(max_length=150, verbose_name='Apellido')),
                ('fecha_ingreso', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Ingreso')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización')),
                ('fecha_emision', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Emisión')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pago')),
                ('fecha_vto', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Vencimiento')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('estado', models.BooleanField(default=True)),
                ('pagado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cheque',
                'verbose_name_plural': 'Cheques',
                'db_table': 'cheque',
                'ordering': ['id'],
            },
        ),
    ]
