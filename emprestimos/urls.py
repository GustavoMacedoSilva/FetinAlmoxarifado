from django.urls import include, path
from .views import EmprestimoView, EmprestimoDetalhes, createEmprestimo


urlpatterns = [
    path('',EmprestimoView, name='emprestimo'),
    path('aluno/<int:pk>/',EmprestimoDetalhes, name='detalhes' ),
    path('cadastrar/', createEmprestimo, name='cadastrar-emprestimo'),
]