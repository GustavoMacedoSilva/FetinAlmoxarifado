from django.urls import path
from .views import HomeView, EquipamentosList, ComponenteList, redirect_to_equipamentos

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('home/', HomeView.as_view(), name='home_page'),
    path('', redirect_to_equipamentos, name = 'inventario_redirect'),
    path('equipamentos/', EquipamentosList.as_view(), name='Listar-Equipamentos'),
    path('componentes/', ComponenteList.as_view(), name='Listar-Componentes'),
]