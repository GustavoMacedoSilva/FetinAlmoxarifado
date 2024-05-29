# Generated by Django 5.0.4 on 2024-05-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('nome', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('matricula', models.IntegerField()),
                ('curso', models.CharField(max_length=50)),
                ('data_de_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]