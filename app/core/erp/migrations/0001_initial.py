# Generated by Django 4.2.1 on 2023-06-01 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('fecha_ingreso', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Ingreso')),
                ('fecha_creacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización')),
                ('edad', models.PositiveIntegerField(default=0)),
                ('sueldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('estado', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]
