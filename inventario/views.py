from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Equipamento, Componente

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_page.html'

class EquipsView(TemplateView):
    template_name = 'equipamentos.html'


########## LISTA ##########

class EquipamentosList(ListView):
    model = Equipamento
    template_name = 'equipamentos.html'

class ComponenteList(ListView):
    model = Componente
    template_name = 'componentes.html'