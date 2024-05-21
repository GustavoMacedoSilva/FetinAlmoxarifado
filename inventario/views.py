from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_page.html'

class EquipsView(TemplateView):
    template_name = 'equipamentos.html'
