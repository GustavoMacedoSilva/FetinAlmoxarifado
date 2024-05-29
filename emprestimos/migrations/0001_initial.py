# Generated by Django 5.0.4 on 2024-05-21 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=50)),
                ('data_de_retirada', models.DateField(verbose_name='Data de Retirada')),
                ('data_de_devolucao', models.DateField(verbose_name='Data de Devolução')),
                ('aluno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='autenticacao.aluno')),
                ('funcionario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='autenticacao.funcionario')),
            ],
        ),
    ]