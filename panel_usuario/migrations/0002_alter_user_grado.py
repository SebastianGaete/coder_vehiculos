# Generated by Django 4.2.4 on 2023-08-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grado',
            field=models.CharField(choices=[('Carabinero', 'Carabinero'), ('Cabo 2ro.', 'Cabo 2ro.'), ('Cabo 1ro.', 'Cabo 1ro.')], max_length=10),
        ),
    ]
