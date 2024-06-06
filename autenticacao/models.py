from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, unique=True)
    email= models.EmailField(unique=True, null=True)
    is_aluno = models.BooleanField(default=False)
    is_funcionario =models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    matricula = models.IntegerField(primary_key=True)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return "user : {}\nmatricula : {}\ncurso : {}".format(self.user, self.matricula, self.curso)
    
class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.IntegerField(primary_key=True, unique=True)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return "user : {}\nid : {}\ncargo : {}".format(self.user, self.id, self.cargo) 
    