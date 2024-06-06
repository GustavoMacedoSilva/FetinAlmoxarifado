from django.urls import include, path
from .views import loginAlmoxarife, loginAluno,logoutUser, createUserAluno, createUserAlmoxarife, createFuncionario

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('almoxarife/', loginAlmoxarife, name='loginAlmoxarife'),
    path('aluno/', loginAluno, name='loginAluno'),
    path('logout/', logoutUser, name='logout'),
    path('registrarUser/', createUserAluno, name='userCreation'),
    path('registrarUserFuncionario/', createUserAlmoxarife, name='userCreationFuncionario'),
    path('registrarFuncionario/', createFuncionario, name='funcionarioCreation')
]