from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.erp.forms import ChequeForm
from core.erp.models import Cheque, Banco, Proveedor
from django.forms.models import model_to_dict


class ChequeListView(TemplateView):
    template_name = 'cheque/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for cheque in Cheque.objects.all():
                    cheque_dict = model_to_dict(cheque)

                    # Obtener el nombre del banco
                    banco = Banco.objects.get(pk=cheque.banco_id)
                    cheque_dict['banco'] = banco.id
                    # Obtener la razón social del proveedor
                    proveedor = Proveedor.objects.get(pk=cheque.proveedor_id)
                    cheque_dict['proveedor'] = proveedor.id

                    cheque_dict['valor'] = cheque.valor
                    cheque_dict['fecha_emision'] = cheque.fecha_emision
                    cheque_dict['fecha_pago'] = cheque.fecha_pago
                    cheque_dict['fecha_vto'] = cheque.fecha_vto
                    data.append(cheque_dict)
            elif action == 'add':
                cheque = Cheque()
                cheque.numero = request.POST['numero']
                cheque.banco_id = request.POST['banco']
                cheque.proveedor_id = request.POST['proveedor']
                cheque.valor = request.POST['valor']
                cheque.save()
            elif action == 'edit':
                cheque = Cheque.objects.get(pk=request.POST['id'])
                cheque.numero = request.POST['numero']
                cheque.banco_id = request.POST['banco']
                cheque.proveedor_id = request.POST['proveedor']
                cheque.valor = request.POST['valor']
                cheque.save()
            elif action == 'delete':
                cheque = Cheque.objects.get(pk=request.POST['id'])
                cheque.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cheques'
        context['list_url'] = reverse_lazy('erp:cheque_list')
        context['entity'] = 'Cheques'
        context['form'] = ChequeForm()

        return context
