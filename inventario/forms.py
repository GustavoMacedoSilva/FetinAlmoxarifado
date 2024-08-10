from .models import Equipamento, Componente
from django.forms import ModelForm
from django import forms

class CreateEquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ['id','nome','descricao','localizacao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

class CreateComponenteForm(ModelForm):
    class Meta:
        model = Componente
        fields = ['nome','unidade_de_medida','valor','localizacao']

class EditEquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome','descricao','localizacao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

class EditComponenteForm(ModelForm):
    class Meta:
        model = Componente
        fields = ['nome','unidade_de_medida','valor','localizacao']