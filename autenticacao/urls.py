from django.urls import path
from .views import loginAlmoxarife, loginAluno,logoutUser, createUserAluno, createUserAlmoxarife

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('almoxarife/', loginAlmoxarife, name='loginAlmoxarife'),
    path('aluno/', loginAluno, name='loginAluno'),
    path('logout/', logoutUser, name='logout'),
    path('registrarUserAluno/', createUserAluno, name='userCreation'),
    path('registrarUserFuncionario/', createUserAlmoxarife, name='userCreationFuncionario'),
]