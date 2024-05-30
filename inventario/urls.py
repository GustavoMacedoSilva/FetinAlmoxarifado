from django.urls import path, include
from .views import EquipamentosList, ComponenteList, redirect_to_equipamentos



urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('equipamentos/', EquipamentosList.as_view(), name='Listar-Equipamentos'),
    path('componentes/', ComponenteList.as_view(), name='Listar-Componentes'),
    path('', redirect_to_equipamentos, name = 'inventario_redirect'),
]