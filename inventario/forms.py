from .models import Equipamento, Componente
from django.forms import ModelForm
from django import forms

class createEquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ['id','nome','descricao','localizacao']
    #id = forms.IntegerField()
    #nome = forms.CharField(max_length=50)
    #descricao = forms.CharField(max_length=500)
    #localizacao = forms.CharField(max_length=50)

class createComponenteForm(ModelForm):
    class Meta:
        model = Componente
        fields = ['nome','unidade_de_medida','valor','localizacao']