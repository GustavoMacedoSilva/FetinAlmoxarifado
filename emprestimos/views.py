from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import redirect

# Create your views here.

class EmprestimoView(TemplateView):
    template_name = 'emprestimos_almoxarife.html'
