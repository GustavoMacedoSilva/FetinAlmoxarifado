from django.shortcuts import render
from django.views.generic import TemplateView

def contato_page(request):
    return render(request, "contato.html")

class HomeView(TemplateView):
    template_name = 'home.html'