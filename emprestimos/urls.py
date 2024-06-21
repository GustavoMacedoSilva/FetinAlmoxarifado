from django.urls import path
from .views import EmprestimoView, EmprestimoDetalhes, createEmprestimo, Test


urlpatterns = [
    path('',EmprestimoView, name='emprestimo'),
    path('aluno/<int:pk>/',EmprestimoDetalhes, name='detalhes' ),
    path('cadastrar/', createEmprestimo, name='cadastrar-emprestimo'),
    path('test/', Test.as_view(), name='test'),
]