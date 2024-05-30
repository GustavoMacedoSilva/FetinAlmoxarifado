from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from django.shortcuts import redirect
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
    fields = ['id','nome','descricao','empretimo']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Equipamentos')

class ComponenteCreate(CreateView):
    model = Componente
    fields = ['id','nome','unidade_de_medida','valor','localizacao']
    template_name = 'cadastros/create_form.html'
    success_url = reverse_lazy('Listar-Componentes')