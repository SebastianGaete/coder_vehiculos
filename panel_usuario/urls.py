from django.urls import path
from .views import *


urlpatterns = [
    path('registro-de-usuarios/', RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('', logear_usuario, name='ingreso_usuario'),
    path('cerrar-sesion/', cerrar_sesion, name= 'cerrar_sesion' ),
    path('cambio-de-contraseña/', cambiar_contraseña, name='cambio_contraseña')
]