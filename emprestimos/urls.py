from django.urls import include, path
from .views import EmprestimoView, EmprestimoDetalhes


urlpatterns = [
    path('',EmprestimoView, name='emprestimo'),
    path('/aluno',EmprestimoDetalhes.as_view(), name='detalhes' ),
]