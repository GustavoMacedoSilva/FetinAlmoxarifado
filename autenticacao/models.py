from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField(primary_key=True)
    curso = models.CharField(max_length=50)
    data_de_nascimento = models.DateField()
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def __str__(self):
        return "nome : {}\nmatricula : {}\ncurso : {}\ndata de nascimento :  {}\nemail : {}".format(self.nome, self.matricula, self.curso, self.data_de_nascimento, self.email)
    
class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return "id : {}\nnome : {}\ncargo : {}".format(self.id, self.nome, self.cargo) 
    