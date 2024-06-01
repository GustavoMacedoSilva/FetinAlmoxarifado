from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
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
    fields = ['id','nome','descricao','emprestimo']
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
    fields = ['id','nome','descricao','emprestimo']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Equipamentos')

class ComponenteUpdate(UpdateView):
    model = Componente
    fields = ['id','nome','unidade_de_medida','valor','localizacao']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Componentes')

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