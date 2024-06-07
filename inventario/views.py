from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from emprestimos.models import Emprestimo
from .models import Equipamento, Componente

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

def addToEmprestimo(request, item_id, emprestimo_id):
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

########## Deletess ##########
def equipamentoDelete(request, item_id):
    if request.method == 'POST':
        item = Equipamento.objects.get(pk=item_id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def componenteDelete(request, item_id):
    if request.method == 'POST':
        item = Componente.objects.get(pk=item_id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)