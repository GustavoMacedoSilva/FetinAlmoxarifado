from django.urls import include, path
from .views import loginAlmoxarife, loginAluno,logoutUser

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('almoxarife/', loginAlmoxarife, name='loginAlmoxarife'),
    path('aluno/', loginAluno, name='loginAluno'),
    path('logout/', logoutUser, name='logout'),
]