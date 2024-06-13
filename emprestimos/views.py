from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Emprestimo
from autenticacao.models import User, Aluno
from inventario.models import Componente, Equipamento, Emprestimo_has_components
from django.urls import reverse_lazy
from .forms import createEmprestimoForm

def EmprestimoView(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    alunos = Aluno.objects.filter(Q(user__username__icontains=q))[:8]

    # Coletar todos os empréstimos e ordenar pela ordem de criação (id)
    emprestimos = Emprestimo.objects.all().order_by('-id')

    # Coletar todos os equipamentos relacionados a esses empréstimos
    equipamentos = Equipamento.objects.filter(emprestimo__in=emprestimos)
    componentes = Emprestimo_has_components.objects.filter(emprestimo__in=emprestimos)

    # Coletar os alunos com empréstimos mais recentes
    alunos_com_emprestimos = Aluno.objects.filter(emprestimo__isnull=False).distinct()

    # Ordenar alunos com base no empréstimo mais recente (id)
    alunos_com_emprestimos = sorted(alunos_com_emprestimos, key=lambda aluno: aluno.emprestimo_set.order_by('-id').first().id, reverse=True)

    context = {
        'alunos': alunos,
        'equipamentos': equipamentos,
        'emprestimos': emprestimos,
        'componentes': componentes,
        'alunos_com_emprestimos': alunos_com_emprestimos,
    }
    return render(request, 'emprestimos_almoxarife.html', context)

def EmprestimoDetalhes(request, pk):
    try:
        aluno = Aluno.objects.get(matricula=pk)
    except Aluno.DoesNotExist:
        return redirect('home_page')
    
    emprestimos = Emprestimo.objects.filter(aluno=aluno).order_by('-id')

    if not emprestimos.exists():
        return redirect('home_page')

    equipamentos = Equipamento.objects.filter(emprestimo__in=emprestimos)
    componentes = Emprestimo_has_components.objects.filter(emprestimo__in=emprestimos)

    # Ordenar alunos com base no empréstimo mais recente (id)
    alunos_com_emprestimos = Aluno.objects.filter(emprestimo__isnull=False).distinct()
    alunos_com_emprestimos = sorted(alunos_com_emprestimos, key=lambda aluno: aluno.emprestimo_set.order_by('-id').first().id, reverse=True)

    context = {
        'aluno': aluno,
        'equipamentos': equipamentos,
        'emprestimos': emprestimos,
        'componentes': componentes,
        'alunos_com_emprestimos': alunos_com_emprestimos,
    }
    return render(request, 'detalhes.html', context)

#def createEmprestimo(request):
    if request.method == 'POST':
        form = createEmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save()
            equipamentos = form.cleaned_data['equipamentos']
            for equipamento in equipamentos:
                equipamento.emprestimo = emprestimo
                equipamento.save()
    else:
        form = createEmprestimoForm()
    return render(request, 'formularios/createEmprestimoForm.html', {'form': form})
def createEmprestimo(request):
    if request.method == 'POST':
        form = createEmprestimoForm(request.POST)
        if form.is_valid():
            estado = form.cleaned_data['estado']
            data_de_devolucao = form.cleaned_data['data_de_devolucao']
            funcionario = form.cleaned_data['funcionario']
            aluno = form.cleaned_data['aluno']
            equipamentos = form.cleaned_data['equipamentos']
            componentes = form.cleaned_data['componentes']

            emprestimo = Emprestimo.objects.create(data_de_devolucao=data_de_devolucao, estado=estado, aluno=aluno, funcionario=funcionario)
            for equipamento in equipamentos:
                equipamento.emprestimo = emprestimo
                equipamento.save()
            
            for componente, quantidade in componentes:
                Emprestimo_has_components.objects.create(emprestimo=emprestimo, componente=componente, quantidade=quantidade)
            
            return redirect('emprestimo')  
    else:
        form = createEmprestimoForm()
    return render(request, 'formularios/createEmprestimoForm.html', {'form': form})