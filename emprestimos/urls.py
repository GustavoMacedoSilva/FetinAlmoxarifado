from django.urls import path
from .views import EmprestimoView, EmprestimoDetalhes, createEmprestimo, testView, deleteEmprestimo, editEmprestimo


urlpatterns = [
    path('',testView, name='emprestimo'),
    path('aluno/<int:pk>/',EmprestimoDetalhes, name='detalhes' ),

    path('cadastrar/', createEmprestimo, name='cadastrar-emprestimo'),
    path('delete-emprestimo/<str:pk>', deleteEmprestimo, name="delete-emprestimo"),
    path('edit-emprestimo/<str:pk>', editEmprestimo, name="edit-emprestimo"),
    
    
]