from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Emprestimo
from autenticacao.models import User,Aluno

# Create your views here.

def EmprestimoView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    aluno= Aluno.objects.filter(
        Q(user__username__icontains=q) 
    )[:8] #get(esp),filter(multiecificoplos especifico),exclude

    context = {'aluno': aluno}
    return render(request, 'emprestimos_almoxarife.html', context)
    
