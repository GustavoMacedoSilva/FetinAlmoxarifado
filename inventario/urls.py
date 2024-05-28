from django.urls import path
from .views import HomeView, EquipamentosList, ComponenteList, redirect_to_equipamentos
from autenticacao.views import loginPage, logoutUser

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('', HomeView.as_view(), name='home_page'),
    path('equipamentos/', EquipamentosList.as_view(), name='Listar-Equipamentos'),
    path('componentes/', ComponenteList.as_view(), name='Listar-Componentes'),
    path('login/', loginPage, name='login')
]