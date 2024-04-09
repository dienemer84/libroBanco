from datetime import datetime

from django.forms import *

from core.erp.models import Cheque, Proveedor, Banco


class ChequeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cheque
        fields = '__all__'
        widgets = {
            'banco': Select(
            ),
            'numero': TextInput(
                attrs={
                    'placeholder': 'Ingrese el número de cheque',
                }
            ),
            'proveedor': Select(
            ),
            'fecha_emision': DateInput(format='%Y-%m-%d',
                                       attrs={
                                           'value': datetime.now().strftime('%Y-%m-%d'),
                                       }
                                       ),
            'fecha_pago': DateInput(format='%Y-%m-%d',
                                    attrs={
                                        'value': datetime.now().strftime('%Y-%m-%d'),
                                    }
                                    ),
            'fecha_vto': DateInput(format='%Y-%m-%d',
                                   attrs={
                                       'value': datetime.now().strftime('%Y-%m-%d'),
                                   }
                                   ),
            'valor': TextInput(
                attrs={
                    'placeholder': 'Ingrese el imporrte',
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

