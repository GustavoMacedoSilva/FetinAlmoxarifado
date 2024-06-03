from django.urls import include, path
from .views import EmprestimoView, EmprestimoDetalhes


urlpatterns = [
    path('',EmprestimoView, name='emprestimo'),
    path('aluno/<int:pk>/',EmprestimoDetalhes, name='detalhes' ),
]