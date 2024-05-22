from django.urls import path
from .views import HomeView, EquipamentosList, ComponenteList

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('', HomeView.as_view(), name = 'home_page'),
    path('equipamentos/', EquipamentosList.as_view(), name='Listar-Equipamentos'),
    path('componentes/', ComponenteList.as_view(), name='Listar-Componentes'),
]