from django.urls import include, path
from .views import EmprestimoView


urlpatterns = [
    path('',EmprestimoView.as_view(), name='emprestimo'),
]