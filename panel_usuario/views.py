from .models import User
from .forms import SetPasswordForm
from .forms import UserCreationFormModificated

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
# @method_decorator(login_required,  name='dispatch')
class RegistrarUsuario(CreateView):
    model = User
    form_class = UserCreationFormModificated
    template_name = 'registrar_usuario.html'
    success_url = reverse_lazy('ingreso_usuario')

    def form_valid(self, form):
        try:
            nuevo_usuario = form.save(commit=False)
            nuevo_usuario.codigo_funcionario = self.request.POST['codigo_funcionario'].upper()

            if nuevo_usuario.codigo_funcionario == '000000-F':
                nuevo_usuario.is_superuser = True
                nuevo_usuario.is_staff = True
            nuevo_usuario.save()
            return super().form_valid(form)
        
        except IntegrityError:
            messages.error(self.request, "Código de funcionario ya existente!")
            return super().form_invalid(form)


def logear_usuario(request):
    form = AuthenticationForm(request.POST)
    if request.method == 'POST':
        codigo_funcionario = request.POST['codigo_funcionario']
        password = request.POST['password']

        autentificacion = authenticate(request=request, codigo_funcionario=codigo_funcionario, password=password)

        if autentificacion is not None:
            login(request, autentificacion)
            return redirect('home')
        else:
            messages.error(request, "Error de autentificación")
            return render (request, 'logear_usuario.html', {'form':form})
    else:
        return render (request, 'logear_usuario.html', {'form':form})



def cerrar_sesion(request):
    logout(request)
    return redirect('ingreso_usuario')


@login_required
def cambiar_contraseña(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingreso_usuario')
        else:
            return render(request, 'cambiar_password.html', {'form': form})

    form = SetPasswordForm(user)
    return render(request, 'cambiar_password.html', {'form': form})
    
