from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.erp.forms import BancoForm
from core.erp.models import Banco
from django.forms.models import model_to_dict


class BancoListView(TemplateView):
    template_name = 'banco/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Banco.objects.all():
                    data.append(model_to_dict(i))
            elif action == 'add':
                banco = Banco()
                banco.nombre = request.POST['nombre']
                banco.detalle = request.POST['detalle']
                banco.save()
            elif action == 'edit':
                banco = Banco.objects.get(pk=request.POST['id'])
                banco.nombre = request.POST['nombre']
                banco.detalle = request.POST['detalle']
                banco.save()
            elif action == 'delete':
                banco = Banco.objects.get(pk=request.POST['id'])
                banco.delete()
            else:
                data['error'] = 'Invalid action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Bancos'
        context['list_url'] = reverse_lazy('erp:banco_list')
        context['entity'] = 'Bancos'
        context['form'] = BancoForm()
        return context
