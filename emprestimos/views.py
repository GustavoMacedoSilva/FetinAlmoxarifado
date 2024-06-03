from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Emprestimo
from autenticacao.models import User, Aluno
from inventario.models import Componente, Equipamento, Emprestimo_has_components

# Create your views here.

def EmprestimoView(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    alunos = Aluno.objects.filter(
        Q(user__username__icontains=q)
    )[:8]

    # Coletar todos os empréstimos relacionados aos alunos filtrados
    emprestimos = Emprestimo.objects.filter(aluno__in=alunos)

    # Coletar todos os equipamentos relacionados a esses empréstimos
    equipamentos = Equipamento.objects.filter(emprestimo__in=emprestimos)

    componentes = Emprestimo_has_components.objects.filter(emprestimo__in=emprestimos)

    context = {
        'alunos': alunos,
        'equipamentos': equipamentos,
        'emprestimos': emprestimos,
        'componentes': componentes,
    }
    return render(request, 'emprestimos_almoxarife.html', context)

class EmprestimoDetalhes(TemplateView):
    template_name = 'detalhes.html'
