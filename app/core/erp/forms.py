from datetime import datetime

from django.forms import *
from django import forms
from core.erp.models import Cheque, Proveedor, Banco


class ChequeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].widget.attrs['autofocus'] = True
        # Formatear la fecha recuperada al formato esperado por el widget
        if self.instance.fecha_emision:
            self.initial['fecha_emision'] = self.instance.fecha_emision.strftime('%d-%m-%Y')
            self.initial['fecha_pago'] = self.instance.fecha_pago.strftime('%d-%m-%Y')
            self.initial['fecha_vto'] = self.instance.fecha_vto.strftime('%d-%m-%Y')
            # Puedes hacer lo mismo para otros campos de fecha si es necesario

    class Meta:
        model = Cheque
        fields = '__all__'
        widgets = {
            'banco': Select(
            ),
            'comprobantes' : TextInput(
                attrs={
                    'placeholder': 'Ingrese los números de comprobantes',
                }
            ),
            'op': TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de OP vinculado',
                }
            ),
            'numero': TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de cheque',
                }
            ),
            'proveedor': Select(
            ),
            'fecha_emision': forms.DateInput(attrs={}),
            'fecha_pago': forms.DateInput(attrs={}),
            'fecha_vto': forms.DateInput(attrs={}),
            'valor': TextInput(
                attrs={
                    'placeholder': 'Ingrese el importe',
                }
            )
        }
        exclude = ['pagado', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProvedForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['razonsocial'].widget.attrs['autofocus'] = True

    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'razonsocial': TextInput(),
            'cuit': TextInput(
                attrs={
                    'placeholder': 'Ingrese el CUIT',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class BancoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Banco
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del banco origen',
                }
            ),

            'detalle': TextInput(
                attrs={
                    'placeholder': 'Ingrese algún detalle importante',
                }
            )
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

