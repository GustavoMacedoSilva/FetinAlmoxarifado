# Generated by Django 5.0.4 on 2024-06-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_rename_empretimo_equipamento_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='localizacao',
            field=models.CharField(default='Gaveta de Equipamentos', max_length=50, verbose_name='Localização'),
            preserve_default=False,
        ),
    ]
