from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from emprestimos.models import Emprestimo
from .models import Equipamento, Componente, Emprestimo_has_components
from .forms import createEquipamentoForm, createComponenteForm
from django.db import IntegrityError

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_page.html'

def redirect_to_equipamentos(request):
    return redirect('Listar-Equipamentos')

########## LISTA ##########

class EquipamentosList(ListView):
    model = Equipamento
    template_name = 'equipamentos.html'

class ComponenteList(ListView):
    model = Componente
    template_name = 'componentes.html'

########## Cadastros ##########
def equipamentoCreate(request):
    if request.method == 'POST':
        form = createEquipamentoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('Listar-Equipamentos')
            except IntegrityError:
                form.add_error('id', 'Não é possivel criar um novo equipamento com um ID igual ao de outro ja existente')
    else:
        form = createEquipamentoForm()        
    return render(request, 'formularios/createEquipamento.html', {'form':form})

def componenteCreate(request):
    if request.method == 'POST':
        form = createComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Listar-Componentes')
    else:
        form = createComponenteForm()
    return render(request, 'formularios/createComponente.html', {'form':form})
            

class EquipamentoCreate(CreateView):
    model = Equipamento
    fields = ['id','nome','descricao','localizacao','emprestimo']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Equipamentos')

class ComponenteCreate(CreateView):
    model = Componente
    fields = ['id','nome','unidade_de_medida','valor','localizacao']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Componentes')

########## Updates ##########
class EquipamentoUpdate(UpdateView):
    model = Equipamento
    fields = ['id','nome','descricao','localizacao','emprestimo']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Equipamentos')

class ComponenteUpdate(UpdateView):
    model = Componente
    fields = ['nome','unidade_de_medida','valor','localizacao']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Componentes')

def addEquipamentoToEmprestimo(request, item_id, emprestimo_id):
    if request.method == 'POST':
        try:
            item = Equipamento.objects.get(pk=item_id)
        except:
            return JsonResponse({'success': False}, status=400)
        try:
            emprestimo = Emprestimo.objects.get(pk=emprestimo_id)
        except:
            return JsonResponse({'success': False}, status=400)
        item.emprestimo = emprestimo
        item.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def addComponenteToEmprestimo(request, item_id, emprestimo_id, quantidade):
    if request.method == 'POST':
        try:
            item = Componente.objects.get(pk=item_id)
        except:
            return JsonResponse({'success': False}, status=400)
        try:
            emprestimo = Emprestimo.objects.get(pk=emprestimo_id)
        except:
            return JsonResponse({'success': False}, status=400)
        Emprestimo_has_components.objects.create(
            emprestimo = emprestimo,
            componente = item,
            quantidade = quantidade
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


########## Deletess ##########
def equipamentoDelete(request, item_id):
    if request.method == 'POST':
        item = Equipamento.objects.get(pk=item_id)
        if item.emprestimo != None:
            return JsonResponse({'success': False, 'error': 405}, status=400)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def componenteIsEmprestimo(item_id):
    try:
        test = Emprestimo_has_components.objects.get(pk=item_id)
    except Emprestimo_has_components.DoesNotExist:
        test = False
    return test

def componenteDelete(request, item_id):
    if componenteIsEmprestimo(item_id) != False:
        return JsonResponse({'success': False, 'error': 405}, status=400)
    if request.method == 'POST':
        item = Componente.objects.get(pk=item_id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)