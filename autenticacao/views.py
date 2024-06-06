from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Aluno, Funcionario, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import creationUserForm, creationAlunoForm, creationUserFormFuncionario, creationAlmoxarifeForm

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

def logoutUser(request):
    logout(request)
    return redirect('home_page')

def createUserAluno(request):
    form = creationUserForm()
    if request.method == 'POST':
        form = creationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            matricula = request.POST.get('matricula')
            curso = request.POST.get('curso')
            Aluno.objects.create(
                user=user,
                matricula=matricula,
                curso=curso,
            )
            return redirect('home_page')
    context = {'form': form}
    return render(request, 'autenticacao/create_user.html', context)


def createUserAlmoxarife(request):
    form = creationUserFormFuncionario()
    
    if request.method == 'POST':
        form = creationUserFormFuncionario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarioCreation')
            
    context = {'form':form}        
    return render(request, 'autenticacao/create_userFuncionario.html', context)

def createFuncionario(request):
    form = creationAlmoxarifeForm()
    
    if request.method == 'POST':
        form = creationAlmoxarifeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    context = {'form': form}
    return render(request, 'autenticacao/createFuncionario.html', context)