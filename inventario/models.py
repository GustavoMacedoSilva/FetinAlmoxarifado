from django.db import models
from emprestimos.models import Emprestimo

# Create your models here.

class Componente(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=50)
    unidade_de_medida = models.CharField(max_length=50, verbose_name='Unidade de Medida')
    valor = models.DecimalField(decimal_places=4, max_digits=16)
    localizacao = models.CharField(max_length=50, verbose_name='Localização')
    
    def __str__(self):
        return "nome : {}\nunidade de medida : {}\nvalor : {}\nlocalizacao : {}".format(self.nome,self.unidade_de_medida,self.valor,self.localizacao)
    

class Equipamento(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500,verbose_name='Descrição')
    localizacao = models.CharField(max_length=50, verbose_name='Localização')
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True) 

    def __str__(self):
        return "id : {}\nnome : {}\ndescrição : {}\nlocalizacao : {}\nemprestimo : {}".format(self.id, self.nome, self.descricao, self.localizacao, self.emprestimo)
    
class Emprestimo_has_components(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    