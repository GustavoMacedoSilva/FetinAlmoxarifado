from django.forms import ModelForm
from django import forms
from .models import Emprestimo
from autenticacao.models import Aluno
from inventario.models import Equipamento, Componente
from django.forms.widgets import NumberInput

class createEmprestimoForm(ModelForm):
    #ESTADOS = [
    #    ('Ativo','Ativo'),
    #    ('Pendente', 'Pendente')
    #    ]
    #estado = forms.ChoiceField(choices=ESTADOS,widget=forms.RadioSelect)
    data_de_devolucao = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),required=True)

    aluno = forms.ModelChoiceField(
        queryset=Aluno.objects.all(),
        widget=forms.Select(),
    ),
    equipamentos = forms.ModelMultipleChoiceField(
        queryset=Equipamento.objects.all(),
        initial=0,
        required=False
    )
    componentes = forms.ModelMultipleChoiceField(
        queryset=Componente.objects.all(),
        initial=0,
        required=False
    )
    class Meta:
        model = Emprestimo
        fields = ['data_de_devolucao','aluno']

#class createEmprestimoForm(ModelForm):
#    estado = forms.CharField(required=True)
#    data_de_devolucao = forms.DateField(required=True)
#    funcionario_pk = forms.IntegerField(label='ID do Funcionario responsavel: ', required=True)
#    aluno_pk = forms.IntegerField(label='Matricula do Aluno: ', required=True)
#    equipamentos_pks = forms.CharField(label='IDs dos equipamentos', widget=forms.Textarea, help_text="Insira os IDs dos equipamentos separados por vírgula", required=False)
#    componentes_pks = forms.CharField(label='IDs dos componentes',widget=forms.Textarea, help_text="Insira os IDs dos componentes a serem inseridos separados por vírgula", required=False)

#    class Meta:
#        model = Emprestimo
#        fields = ['estado', 'data_de_devolucao']

#    def clean(self):
#        cleaned_data = super().clean() 
#        funcionario_pk = cleaned_data.get('funcionario_pk')
#        aluno_pk = cleaned_data.get('aluno_pk')
#        equipamentos_pks = cleaned_data.get('equipamentos_pks')
#        componentes_pks = cleaned_data.get('componentes_pks')

#        try:
#            funcionario = Funcionario.objects.get(pk=funcionario_pk)
#        except Funcionario.DoesNotExist:
#            self.add_error('funcionario_pk', 'Funcionario com esse ID não existe')

#        try:
#            aluno = Aluno.objects.get(pk=aluno_pk)
#        except Aluno.DoesNotExist:
#            self.add_error('aluno_pk', 'Aluno com essa matricula não existe')
        
#        equipamentos = []
#        if equipamentos_pks != '':
#            for pk in equipamentos_pks.split(','):
#                try:
#                    equipamento = Equipamento.objects.get(pk=pk)
#                    equipamentos.append(equipamento)
#                except Equipamento.DoesNotExist:
#                    self.add_error('equipamentos_pks', f'Equipamento com ID: {pk.strip()} não existe')

#        componentes = []
#        if componentes_pks != '':
#            for item in componentes_pks.split(','):
#                try:
#                    pk, quantidade = item.split(':')
#                    componente = Componente.objects.get(pk=pk)
#                    componentes.append((componente, int(quantidade.strip())))
#                except Componente.DoesNotExist:
#                    self.add_error('componentes_pks', f'Componente com ID {pk.strip()} não existe')
#                except ValueError:
#                    self.add_error('componentes_pks', f'Formato inválido para o componente: {item}')
    
#        if not self.errors:
#            cleaned_data['funcionario'] = funcionario
#            cleaned_data['aluno'] = aluno
#            cleaned_data['equipamentos'] = equipamentos
#            cleaned_data['componentes'] = componentes

#        return cleaned_data