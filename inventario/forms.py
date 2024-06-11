from .models import Equipamento
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