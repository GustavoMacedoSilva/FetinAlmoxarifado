from django.urls import path
from .views import equipamentosList, componenteList 
from .views import equipamentoCreate, componenteCreate
from .views import equipamentoUpdate, componenteUpdate
from .views import equipamentoDelete, componenteDelete
from .views import addEquipamentoToEmprestimo, addComponenteToEmprestimo
from .views import redirect_to_equipamentos

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    ######## Tabelas ########
    path('equipamentos/', equipamentosList, name='Listar-Equipamentos'),
    path('componentes/', componenteList, name='Listar-Componentes'),
    ######## Cadastros ########
    path('cadastrar/equipamento/', equipamentoCreate, name = 'Cadastrar-Equipamento'),
    path('cadastrar/componente/', componenteCreate, name = 'Cadastrar-Componente'),
    ######## Editar ########
    path('editar/equipamento/<int:pk>/', equipamentoUpdate, name = 'Editar-Equipamento'),
    path('editar/componente/<int:pk>/', componenteUpdate, name = 'Editar-Componente'),
    path('equipamentos/addToEmprestimo/<int:item_id>/<int:emprestimo_id>/', addEquipamentoToEmprestimo, name='add-to-emprestimo'),
    path('componentes/addToEmprestimo/<int:item_id>/<int:emprestimo_id>/<int:quantidade>/', addComponenteToEmprestimo, name='add-to-emprestimo'),
    ######## Deletar ########
    path('equipamentos/delete/<int:item_id>/', equipamentoDelete, name='Deletar-Equipamento'),
    path('componentes/delete/<int:item_id>/', componenteDelete, name='Deletar-Componente'),
    ######## Redirect ########
    path('', redirect_to_equipamentos, name = 'inventario_redirect'),
]