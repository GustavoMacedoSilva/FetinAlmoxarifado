from django.urls import include, path
from .views import EmprestimoView


urlpatterns = [
    path('',EmprestimoView, name='emprestimo'),
]