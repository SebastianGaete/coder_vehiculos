from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    # Formularios para insertar registros
    path('formulario-vehiculo/', CrearVehiculo.as_view(), name='formulario_vehiculo'),
    path('formulario-propietario-vehiculo/<int:id>', CrearPropietario.as_view(), name='formulario_propietario'),
    path('formulario-entrega-vehiculo/<int:id>', EntregaVehiculo.as_view(), name='formulario_entrega_vehiculo'),
    # Filtrados
    path('vehiculos/<tribunal>/', FiltroVehiculosTribunal.as_view(), name='filtro_vehiculos_tribunales'),
    path('vehiculos-entregados', VehiculosEntregados.as_view(), name='vehiculos_entregados'),
    # Detalle vehiculo
    path( 'detalle-vehiculo/<int:id>', DetalleVehiculo.as_view(), name='detalle_vehiculo' ),
    # Modificar vehiculo
    path('modificar-vehiculo/<int:pk>/', ModificarVehiculo.as_view(), name='modificar_vehiculo'),
    # Eliminar Vehículo
    path('eliminar-vehiculo/<int:pk>/', EliminarVehiculo.as_view(), name='eliminar_vehiculo')    
]