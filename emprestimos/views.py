from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Emprestimo
from autenticacao.models import User, Aluno, Funcionario
from inventario.models import Componente, Equipamento, Emprestimo_has_components
from .forms import createEmprestimoForm
from django.utils import timezone

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
    user = request.user

    try:
        aluno = Aluno.objects.get(matricula=pk)
    except Aluno.DoesNotExist:
        return redirect('home_page')

    emprestimos = Emprestimo.objects.filter(aluno=aluno).order_by('-id')

    if not emprestimos.exists():
        return redirect('home_page')

    # Permissão de acesso: Funcionário ou Superusuário
    pode_editar_deletar = user.is_funcionario or user.is_superuser

    equipamentos = Equipamento.objects.filter(emprestimo__in=emprestimos)
    componentes = Emprestimo_has_components.objects.filter(emprestimo__in=emprestimos)

    alunos_com_emprestimos = Aluno.objects.filter(emprestimo__isnull=False).distinct()
    alunos_com_emprestimos = sorted(alunos_com_emprestimos, key=lambda aluno: aluno.emprestimo_set.order_by('-id').first().id, reverse=True)

    context = {
        'aluno': aluno,
        'equipamentos': equipamentos,
        'emprestimos': emprestimos,
        'componentes': componentes,
        'alunos_com_emprestimos': alunos_com_emprestimos,
        'pode_editar_deletar': pode_editar_deletar,  # Passar a variável de controle para o template
    }
    return render(request, 'detalhes.html', context)

########### mexendo com a tabela emprestimo ########### 

def createEmprestimo(request):
    if request.user.is_authenticated and request.user.is_funcionario:
        if request.method == 'POST':
            form = createEmprestimoForm(request.POST)
            if form.is_valid():
                equipamentos = form.cleaned_data['equipamentos']
                componentes = form.cleaned_data['componentes']
                # retorna True caso algum dos equipamentos selecionados pelo usuario ja esteja em algum emprestimo
                equipamentoIsEmprestimo = any(equipamento.emprestimo != None for equipamento in equipamentos)
                
                if not equipamentoIsEmprestimo:
                    emprestimo = form.save(commit=False)
                    funcionario = Funcionario.objects.get(user=request.user)
                    emprestimo.funcionario = funcionario
                    emprestimo.estado = 'Ativo'
                    emprestimo.save()
                    
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
    else:
        return redirect('home_page')
    

def editEmprestimo(request, pk):
    if request.user.is_authenticated and request.user.is_funcionario:
        emprestimo = Emprestimo.objects.get(id=pk)
        
        if request.method == 'POST':
            form = createEmprestimoForm(request.POST, instance=emprestimo)
            if form.is_valid():
                equipamentos = form.cleaned_data['equipamentos']
                componentes = form.cleaned_data['componentes']
                
                equipamentoIsEmprestimo = any(equipamento.emprestimo != None and equipamento.emprestimo != emprestimo for equipamento in equipamentos)
                
                if not equipamentoIsEmprestimo:
                    newEmprestimo = form.save(commit=False)
                    funcionario = Funcionario.objects.get(user=request.user)
                    newEmprestimo.funcionario = funcionario
                    if newEmprestimo.data_de_devolucao < timezone.now().date():
                        newEmprestimo.estado = 'Atrasado'
                    else:
                        newEmprestimo.estado = 'Ativo'
                    newEmprestimo.save()
                    
                    equipamentosRemove = Equipamento.objects.filter(emprestimo=emprestimo)

                    componentesRemove = Emprestimo_has_components.objects.filter(
                        emprestimo=emprestimo
                    )

                    for equipamento in equipamentosRemove:
                        equipamento.emprestimo = None
                        equipamento.save()

                    for componente in componentesRemove:
                        componente.delete()

                    for equipamento in equipamentos:
                        equipamento.emprestimo = emprestimo
                        equipamento.save()
                    
                    for componente in componentes:
                        quantidade = request.POST.get(f'quantidade_{componente.id}', 1)
                        Emprestimo_has_components.objects.create(
                            emprestimo=newEmprestimo,
                            componente=componente,
                            quantidade=quantidade
                        )

                    return redirect('emprestimo')
                else:
                    form.add_error('equipamentos', 'Um ou mais equipamentos selecionados já estão em algum empréstimo, por favor remova-os ou troque')
        else:
            form = createEmprestimoForm(instance=emprestimo)

        return render(request, 'formularios/editEmprestimoForm.html', {'form': form})
    
    else:
        return redirect('home_page')

def deleteEmprestimo(request, pk):
    if request.user.is_authenticated and request.user.is_funcionario:
        emprestimo = Emprestimo.objects.get(id=pk)
        if request.method == 'POST':
            emprestimo.delete()
            return redirect('emprestimo') 
        return render(request, 'delete.html',{'obj':emprestimo})
    else:
        return redirect('home_page')

########### Card ###########
def emprestimosCard(request):
    user = request.user
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    qtd_equipamentos = {}
    qtd_componentes = {}
    emprestimos = []

    if user.is_authenticated:
        if user.is_funcionario or user.is_superuser:
            emprestimos = Emprestimo.objects.filter(
                Q(aluno__user__username__icontains=q) |
                Q(aluno__matricula__icontains=q)
            ).order_by('-id')
            for emprestimo in emprestimos:
                soma_componentes = 0
                qtd_equipamentos[emprestimo.id] = Equipamento.objects.filter(emprestimo=emprestimo).__len__()
                relations = Emprestimo_has_components.objects.filter(emprestimo=emprestimo)
                for relation in relations:
                    soma_componentes += relation.quantidade
                qtd_componentes[emprestimo.id] = soma_componentes
        else:
            aluno = Aluno.objects.get(user=user)
            emprestimos = Emprestimo.objects.filter(aluno=aluno)
            for emprestimo in emprestimos:
                soma_componentes = 0
                qtd_equipamentos[emprestimo.id] = Equipamento.objects.filter(emprestimo=emprestimo).__len__()
                relations = Emprestimo_has_components.objects.filter(emprestimo=emprestimo)
                for relation in relations:
                    soma_componentes += relation.quantidade
                qtd_componentes[emprestimo.id] = soma_componentes

    else:
        return redirect('loginUser')

    context = {
        'emprestimos':emprestimos,
        'qtd_equipamentos':qtd_equipamentos,
        'qtd_componentes':qtd_componentes
    }

    return render(request, 'emprestimo.html', context)
