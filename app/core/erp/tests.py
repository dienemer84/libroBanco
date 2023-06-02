from config.wsgi import *
from core.erp.models import Banco

# listar
# query = Banco.objects.all()
# print(query)


# insertar
# t = Banco(nombre='ICBC')
# t.save()


# edicion
# t = Banco.objects.get(id=1)
# print(t.nombre)


# borrado
# t = Banco.objects.get(pk=2)
# t.delete()

#filtro incluyente
# obj = Banco.objects.filter(nombre__contains='O')
# print(obj)
#
