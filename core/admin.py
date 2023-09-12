from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Tribunal)
class AdminTribunal(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Vehiculo)
class AdminVehiculo(admin.ModelAdmin):
    list_display = ('tipo', 'marca', 'modelo', 'placa_patente', 'disposicion', 'numero_de_parte')

@admin.register(Propietario_vehiculo)
class AdminPropietarioVehiculo(admin.ModelAdmin):
    pass

@admin.register(Entrega_vehiculo)
class AdminEntregaVehiculo(admin.ModelAdmin):
    pass