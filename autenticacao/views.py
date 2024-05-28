from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Aluno, Funcionario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home_page')
    
    if request.method == 'POST':
        nome = request.POST.get('username')
        senha = request.POST.get('password')

        try:
            aluno = Aluno.objects.get(nome=nome)
        except:
            messages.error(request, 'Usuario não existe')

        aluno = authenticate(request, nome=nome, senha=senha)

        if aluno is not None:
            login(request, aluno)
            return redirect('home_page')
        else:
            messages.error(request, 'Usuario ou senha não existe')

    context = {'page': page}

    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_page')

