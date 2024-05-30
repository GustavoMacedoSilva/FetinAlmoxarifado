from django.urls import path
from .views import EquipamentosList, ComponenteList, redirect_to_equipamentos, EquipamentoCreate, ComponenteCreate



urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('equipamentos/', EquipamentosList.as_view(), name='Listar-Equipamentos'),
    path('componentes/', ComponenteList.as_view(), name='Listar-Componentes'),
    path('cadastrar/equipamento/', EquipamentoCreate.as_view(), name = 'Cadastrar-Equipamento'),
    path('cadastrar/componente/',ComponenteCreate.as_view(), name = 'Cadastrar-Componente'),
    path('', redirect_to_equipamentos, name = 'inventario_redirect'),
]