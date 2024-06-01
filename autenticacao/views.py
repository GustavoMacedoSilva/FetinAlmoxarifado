from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Aluno, Funcionario, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def loginAlmoxarife(request):
    page = 'almoxarife'

    if request.user.is_authenticated:
        return redirect('home_page')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario não existe')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Usuario ou senha está incorreta')

    context = {'page': page}

    return render(request, 'autenticacao/login_register.html', context)

def loginAluno(request):
    page = 'aluno'
    context = {'page': page}
    return render(request, 'autenticacao/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home_page')

