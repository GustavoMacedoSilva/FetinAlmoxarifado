from django.db import models
from autenticacao.models import Aluno, Funcionario

# Create your models here.

class Emprestimo(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    estado = models.CharField(max_length=50)
    data_de_retirada = models.DateField(verbose_name='Data de Retirada', auto_now_add=True)
    data_de_devolucao = models.DateField(verbose_name='Data de Devolução')
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return "id : {}\nestado : {}\ndata de devolução : {}\ndata de retirada : {}\naluno : {}\nfuncionario : {}".format(self.id, self.estado, self.data_de_devolucao, self.data_de_retirada, self.aluno, self.funcionario)
