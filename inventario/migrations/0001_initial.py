# Generated by Django 5.0.4 on 2024-06-06 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emprestimos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('unidade_de_medida', models.CharField(max_length=50, verbose_name='Unidade de Medida')),
                ('valor', models.DecimalField(decimal_places=4, max_digits=16)),
                ('localizacao', models.CharField(max_length=50, verbose_name='Localização')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo_has_components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.componente')),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprestimos.emprestimo')),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
                ('localizacao', models.CharField(max_length=50, verbose_name='Localização')),
                ('emprestimo', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='emprestimos.emprestimo')),
            ],
        ),
    ]
