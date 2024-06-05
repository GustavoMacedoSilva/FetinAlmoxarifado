from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Aluno, Funcionario
from django import forms

class creationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
        
class creationAlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        
class creationAlmoxarifeForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        
class creationUserFormFuncionario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff']