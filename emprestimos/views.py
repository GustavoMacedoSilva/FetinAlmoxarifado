from django.views.generic import TemplateView, CreateView, UpdateView, ListView
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
from django.http import JsonResponse

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

########### mexendo com a tabela emprestimo ########### 

def createEmprestimo(request):
    if request.method == 'POST':
        form = createEmprestimoForm(request.POST)
        if form.is_valid():
            equipamentos = form.cleaned_data['equipamentos']
            componentes = form.cleaned_data['componentes']
            # retorna True caso algum dos equipamentos selecionados pelo usuario ja esteja em algum emprestimo
            equipamentoIsEmprestimo = any(equipamento.emprestimo != None for equipamento in equipamentos)
            
            if not equipamentoIsEmprestimo:
                emprestimo = form.save()
                
                for equipamento in equipamentos:
                    equipamento.emprestimo = emprestimo
                    equipamento.save()
                
                for componente in componentes:
                    quantidade = request.POST.get(f'quantidade_{componente.id}', 1)
                    Emprestimo_has_components.objects.create(
                        emprestimo = emprestimo,
                        componente = componente,
                        quantidade = quantidade
                    )

                return redirect('emprestimo')
            else:
                form.add_error('equipamentos', 'Um ou mais equipamentos selecionados ja estão em algum emprestimo, por favor remova-os ou troque')
    else:
        form = createEmprestimoForm()
    return render(request, 'formularios/createEmprestimoForm.html', {'form': form})

def editEmprestimo(request, pk):
    emprestimo = Emprestimo.objects.get(id=pk)
    
    if request.method == 'POST':
        form = createEmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            equipamentos = form.cleaned_data['equipamentos']
            componentes = form.cleaned_data['componentes']
            
            equipamentoIsEmprestimo = any(equipamento.emprestimo != None for equipamento in equipamentos)
            
            if not equipamentoIsEmprestimo:
                emprestimo = form.save()
                
                for equipamento in equipamentos:
                    equipamento.emprestimo = emprestimo
                    equipamento.save()
                
                for componente in componentes:
                    quantidade = request.POST.get(f'quantidade_{componente.id}', 1)
                    Emprestimo_has_components.objects.create(
                        emprestimo=emprestimo,
                        componente=componente,
                        quantidade=quantidade
                    )

                return redirect('emprestimo')
            else:
                form.add_error('equipamentos', 'Um ou mais equipamentos selecionados já estão em algum empréstimo, por favor remova-os ou troque')
    else:
        form = createEmprestimoForm(instance=emprestimo)

    return render(request, 'formularios/editEmprestimoForm.html', {'form': form})

def deleteEmprestimo(request, pk):
    emprestimo = Emprestimo.objects.get(id=pk)
    if request.method == 'POST':
        emprestimo.delete()
        return redirect('emprestimo') 
    return render(request, 'delete.html',{'obj':emprestimo})

########### teste ###########
def testView(request):
    emprestimos = Emprestimo.objects.all()
    qtd_equipamentos = {}
    qtd_componentes = {}
    
    for emprestimo in emprestimos:
        soma_componentes = 0
        qtd_equipamentos[emprestimo.id] = Equipamento.objects.filter(emprestimo=emprestimo).__len__()
        relations = Emprestimo_has_components.objects.filter(emprestimo=emprestimo)
        for relation in relations:
            soma_componentes += relation.quantidade
        qtd_componentes[emprestimo.id] = soma_componentes

    context = {
        'emprestimos':emprestimos,
        'qtd_equipamentos':qtd_equipamentos,
        'qtd_componentes':qtd_componentes
    }

    return render(request, 'test.html', context)
