from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    CHOICES = (
        ('Carabinero',)*2,
        ('Cabo 2do.',)*2,
        ('Cabo 1ro.',)*2,
    )
    username = models.CharField(max_length=150, unique=False)  # Desactivar la unicidad
    email = models.EmailField(unique=True)
    grado = models.CharField(max_length=10,  choices=CHOICES)
    codigo_funcionario = models.CharField(max_length=8, unique=True, verbose_name='Código funcionario')

    def __str__(self):
        return self.grado + " " + self.first_name + " " + self.last_name