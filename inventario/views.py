from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import redirect
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