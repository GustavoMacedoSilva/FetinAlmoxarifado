from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    matricula = models.IntegerField(unique=True)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return "nome : {}\nmatricula : {}\ncurso : {}\ndata de nascimento :  {}\nemail : {}".format(self.nome, self.matricula, self.curso, self.data_de_nascimento, self.email)
    
class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return "id : {}\nnome : {}\ncargo : {}".format(self.id, self.nome, self.cargo) 
    