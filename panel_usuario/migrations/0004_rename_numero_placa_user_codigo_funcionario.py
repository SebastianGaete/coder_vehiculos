# Generated by Django 4.2.4 on 2023-08-19 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_usuario', '0003_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='numero_placa',
            new_name='codigo_funcionario',
        ),
    ]