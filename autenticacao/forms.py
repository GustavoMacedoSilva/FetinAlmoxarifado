from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Aluno
from django import forms

class creationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
        
class creationAlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'