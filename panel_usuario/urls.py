from django.urls import path
from .views import *


urlpatterns = [
    path('registro-de-usuarios/', RegistrarUsuario.as_view(), name='registro_usuario'),
    path('', logear_usuario, name='logear_usuario'),
    path('cerrar-sesion/', cerrar_sesion, name= 'cerrar_sesion' ),
    path('cambio-de-contraseña/', cambiar_contraseña, name='cambiar_contraseña')
]