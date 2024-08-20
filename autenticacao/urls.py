from django.urls import path
from .views import loginUser, logoutUser, createUserAluno, createUserAlmoxarife

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('login/', loginUser, name='loginUser'),
    path('logout/', logoutUser, name='logout'),
    path('registrarUserAluno/', createUserAluno, name='userCreation'),
    path('registrarUserFuncionario/', createUserAlmoxarife, name='userCreationFuncionario'),
]