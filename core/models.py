from django.db import models
from panel_usuario.models import User
from .choices_models import CHOICES_MOTIVO, CHOICES_TIPO, CHOICES_TRIBUNALES, ACTA_ENTREGA
# Create your models here.


class Tribunal(models.Model):
    nombre = models.CharField(unique=True, max_length=60, choices=CHOICES_TRIBUNALES, verbose_name='Nombre de Tribunal')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Tribunal'
        verbose_name_plural = 'Tribunales'

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=60, choices=CHOICES_TIPO)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    placa_patente = models.CharField(max_length=6, unique=True)
    año = models.IntegerField()
    color = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='vehiculos')
    motivo = models.CharField(max_length=100, choices=CHOICES_MOTIVO)
    disposicion = models.ForeignKey(Tribunal, to_field='nombre', on_delete=models.RESTRICT, verbose_name='Disposición')
    fecha_ingreso = models.DateTimeField(verbose_name='Fecha de ingreso')
    numero_de_parte = models.IntegerField(blank=True, null=True, verbose_name='Número parte')
    numero_de_oficio = models.IntegerField(blank=True, null=True, verbose_name='Número oficio')
    acta_entrega = models.CharField(max_length=2, choices=ACTA_ENTREGA)
    observaciones = models.TextField(blank=True, default='Sin observaciones')

    entregado = models.BooleanField(default=False)
    registro_propietario = models.BooleanField(default=False)
    funcionario_receptor = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, related_name='funcionario_receptor')
    funcionario_entrega = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='funcionario_entrega')

    def __str__(self):
        return self.placa_patente
    
    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

class Propietario_vehiculo(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=70)
    rut = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    direccion = models.CharField(max_length=100, blank=True, verbose_name='Dirección')
    comuna = models.CharField(max_length=30, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, to_field='placa_patente', verbose_name='Vehículo')

    def __str__(self):
        return self.nombre + " " + self.apellidos
    
    class Meta:
        verbose_name = 'Propietario vehiculo'
        verbose_name_plural = 'Propietarios de vehículos'
    

class Entrega_vehiculo(models.Model):
    numero_de_oficio = models.IntegerField(verbose_name='Número oficio')
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, to_field='placa_patente', verbose_name='Vehículo')
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=70)
    rut = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10, blank=True, null=True, verbose_name='Teléfono')
    observaciones = models.TextField(blank=True, default='Sin observaciones')
    fecha_entrega_vehiculo = models.DateTimeField(auto_now_add=True)
    funcionario = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.numero_de_oficio)

    class Meta:
        verbose_name = 'Entrega de vehículo'
        verbose_name_plural = 'Entregas de vehículos'
    



