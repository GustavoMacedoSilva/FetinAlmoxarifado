from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aluno, Funcionario, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import creationUserForm, creationUserFormFuncionario

# Create your views here.


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home_page')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Email não existe')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Email ou senha está incorreta')


    return render(request, 'autenticacao/login_register.html')

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
            user = form.save()
            id = request.POST.get('id')
            cargo = request.POST.get('cargo')
            Funcionario.objects.create(
                user=user,
                id=id,
                cargo=cargo,
            )
            return redirect('home_page')
            
    context = {'form':form}        
    return render(request, 'autenticacao/create_userFuncionario.html', context)
