from django.urls import path

from core.erp.views.cheque.views import ChequeListView
from core.erp.views.banco.views import BancoListView
from core.erp.views.proveedor.views import ProveedorListView

app_name = 'erp'

urlpatterns = [
    path('cheque/', ChequeListView.as_view(), name='cheque_list'),
    path('banco/', BancoListView.as_view(), name='banco_list'),
    path('proveedor/', ProveedorListView.as_view(), name='proveedor_list'),
]
