# Generated by Django 5.0.4 on 2024-06-01 17:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_user_is_aluno_user_is_funcionario_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
