from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.erp.forms import ProvedForm
from core.erp.models import Proveedor
from django.forms.models import model_to_dict


class ProveedorListView(TemplateView):
    template_name = 'proveedor/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Proveedor.objects.all():
                    data.append(model_to_dict(i))
            elif action == 'add':
                proveedor = Proveedor()
                proveedor.razonsocial = request.POST['razonsocial']
                proveedor.cuit = request.POST['cuit']
                proveedor.save()
            elif action == 'edit':
                proveedor = Proveedor.objects.get(pk=request.POST['id'])
                proveedor.razonsocial = request.POST['razonsocial']
                proveedor.cuit = request.POST['cuit']
                proveedor.save()
            elif action == 'delete':
                proveedor = Proveedor.objects.get(pk=request.POST['id'])
                proveedor.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proveedores'
        context['list_url'] = reverse_lazy('erp:proveedor_list')
        context['entity'] = 'Proveedor'
        context['idtable'] = 'data'
        context['form'] = ProvedForm()
        return context
