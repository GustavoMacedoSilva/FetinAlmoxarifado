from django.urls import path
from .views import EquipamentosList, ComponenteList 
from .views import EquipamentoCreate, ComponenteCreate
from .views import EquipamentoUpdate, ComponenteUpdate
from .views import equipamentoDelete, componenteDelete
from .views import redirect_to_equipamentos



urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    ######## Tabelas ########
    path('equipamentos/', EquipamentosList.as_view(), name='Listar-Equipamentos'),
    path('componentes/', ComponenteList.as_view(), name='Listar-Componentes'),
    ######## Cadastros ########
    path('cadastrar/equipamento/', EquipamentoCreate.as_view(), name = 'Cadastrar-Equipamento'),
    path('cadastrar/componente/',ComponenteCreate.as_view(), name = 'Cadastrar-Componente'),
    ######## Editar ########
    path('editar/equipamento/<int:pk>/', EquipamentoUpdate.as_view(), name = 'Editar-Equipamento'),
    path('editar/componente/<int:pk>/', ComponenteUpdate.as_view(), name = 'Editar-Componente'),
    ######## Deletar ########
    path('equipamentos/delete/<int:item_id>/', equipamentoDelete, name='Deletar-Equipamento'),
    path('componentes/delete/<int:item_id>/', componenteDelete, name='Deletar-Componente'),
    ######## Redirect ########
    path('', redirect_to_equipamentos, name = 'inventario_redirect')
]