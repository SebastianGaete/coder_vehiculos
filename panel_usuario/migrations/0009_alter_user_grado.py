# Generated by Django 4.2.5 on 2023-09-12 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_usuario', '0008_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grado',
            field=models.CharField(choices=[('Cabo', 'Cabo'), ('Cabo 2do.', 'Cabo 2do.'), ('Cabo 1ro.', 'Cabo 1ro.')], max_length=10),
        ),
    ]
