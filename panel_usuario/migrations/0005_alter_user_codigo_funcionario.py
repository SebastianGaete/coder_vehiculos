# Generated by Django 4.2.4 on 2023-08-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_usuario', '0004_rename_numero_placa_user_codigo_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codigo_funcionario',
            field=models.CharField(max_length=8, unique=True, verbose_name='Código funcionario'),
        ),
    ]
