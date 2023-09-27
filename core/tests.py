from django.test import TestCase
from .models import *

# Create your tests here.
class VehiculoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de datos para todas las pruebas
        Tribunal.objects.create(nombre='Tribunal de Prueba')
        User.objects.create_user(username='usuario_prueba', password='contraseña123')

        Vehiculo.objects.create(
            tipo='Tipo de Prueba',
            marca='Marca de Prueba',
            modelo='Modelo de Prueba',
            placa_patente='ABC123',
            año=2022,
            color='Rojo',
            imagen='vehiculos/prueba.jpg',
            motivo='Motivo de Prueba',
            disposicion=Tribunal.objects.get(nombre='Tribunal de Prueba'),
            fecha_ingreso='2023-08-30 10:00:00',
            numero_de_parte=123,
            numero_de_oficio=456,
            acta_entrega='SI',
            observaciones='Observaciones de Prueba',
            entregado=True,
            registro_propietario=False,
            funcionario_receptor=User.objects.get(username='usuario_prueba'),
            funcionario_entrega=User.objects.get(username='usuario_prueba')
        )


    def test_campos(self):
        vehiculo = Vehiculo.objects.get(id=1)
        self.assertEqual(vehiculo.tipo, 'Tipo de Prueba')
        self.assertEqual(vehiculo.marca, 'Marca de Prueba')
        self.assertEqual(vehiculo.modelo, 'Modelo de Prueba')
        
    def test_default_values(self):
        vehiculo = Vehiculo.objects.get(id=1)
        self.assertEqual(vehiculo.registro_propietario, False)
        self.assertEqual(vehiculo.observaciones, 'Observaciones de Prueba')

        