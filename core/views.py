from .models import Vehiculo, Entrega_vehiculo, Propietario_vehiculo
from .forms import FormularioVehiculo, FormularioPropietarioVehiculo, FormularioEntregaVehiculo

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required



@method_decorator(login_required, name='dispatch')
class Index(ListView):
    model = Vehiculo
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        vehiculos = Vehiculo.objects.filter(entregado=False).order_by('-fecha_ingreso') # Ordenamos por fecha_ingreso (de forma inversa)
        cantidad_vehiculos = vehiculos.count() #Count devuelve un tipo de dato int
        busqueda = self.request.GET.get("buscar")
        page = self.request.GET.get('page', 1)
        try:
            paginador = Paginator(vehiculos, 10)
            vehiculos = paginador.page(page)
        except:
            raise Http404

        if busqueda:
            vehiculos = Vehiculo.objects.filter( Q(entregado=False), Q(placa_patente__icontains=busqueda) | Q(marca__icontains=busqueda) | 
            Q(numero_de_parte__icontains=busqueda) | Q(modelo__icontains=busqueda) | Q(tipo__icontains=busqueda) )
            
            cantidad_vehiculos = vehiculos.count()       
        # icontains no toma distinciones entre mayúsculas o minúsculas

        context['entity'] = vehiculos
        context['cantidad'] =  cantidad_vehiculos
        context['paginator'] = paginador
        return context


@method_decorator(login_required, name='dispatch')
class CrearVehiculo(CreateView):
    model = Vehiculo
    form_class = FormularioVehiculo
    template_name = 'pages/registros/vehiculo.html'
    success_url = reverse_lazy('formulario_vehiculo')

    def form_valid(self, form):
        try:
            global placa_patente
            placa_patente = self.request.POST['placa_patente'].upper()
            vehiculo_nuevo = form.save(commit=False)
            vehiculo_nuevo.funcionario_receptor = self.request.user
            vehiculo_nuevo.placa_patente = placa_patente
            vehiculo_nuevo.save()
            messages.success(self.request, "Registro de vehículo creado con éxito!")
            return super().form_valid(form)
        
        except IntegrityError:
            messages.error(self.request, f"El vehículo con P.P.U. {placa_patente} ya se encuentra registrado.")
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"El vehículo con la P.P.U. que deseas ingresar ya se encuentra registrado.")
        return super().form_invalid(form)

    
@method_decorator(login_required, name='dispatch')
class CrearPropietario(CreateView):
    model  = Propietario_vehiculo
    form_class = FormularioPropietarioVehiculo
    template_name = 'pages/registros/propietario_vehiculo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global vehiculo
        vehiculo = get_object_or_404(Vehiculo, id=self.kwargs['id'])
        return context
    
    def form_valid(self, form):
        vehiculo.registro_propietario = True
        vehiculo.save()

        propietario_asignado = form.save(commit=False)
        propietario_asignado.vehiculo = vehiculo
        propietario_asignado.save()
        messages.success(self.request, "Registro de propietario de vehículo creado con exito!")
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('formulario_propietario', kwargs={'id': vehiculo.id})
    
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error; porfavor verifique que los campos se hayan ingresado de forma correcta e intente de nuevo!" )
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class EntregaVehiculo(CreateView):
    model = Entrega_vehiculo
    form_class = FormularioEntregaVehiculo
    template_name = 'pages/registros/entrega_vehiculo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global vehiculo
        vehiculo = get_object_or_404(Vehiculo, id=self.kwargs['id'])
        return context
    
    def form_valid(self, form):
        vehiculo.funcionario_entrega = self.request.user
        vehiculo.entregado = True
        vehiculo.save()

        registro_entrega = form.save(commit=False)
        registro_entrega.funcionario = self.request.user
        registro_entrega.vehiculo = vehiculo
        registro_entrega.save()
        messages.success(self.request, "Registro de entrega de vehículo creado con exito!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('formulario_entrega_vehiculo', kwargs={'id': vehiculo.id})
    
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error; porfavor verifique que los campos se hayan ingresado de forma correcta e intente de nuevo!" )
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class FiltroVehiculosTribunal(ListView):
    model = Vehiculo
    template_name = 'pages/filtrados/tribunales.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tribunal = self.kwargs['tribunal'] # Con esta sintaxis capturo el parámetro que necesito.
        vehiculos = Vehiculo.objects.filter(disposicion=tribunal, entregado=False).order_by('-fecha_ingreso')
        cantidad_vehiculos = vehiculos.count()
        buscar = self.request.GET.get("buscar")

        if buscar:
           vehiculos = Vehiculo.objects.filter( Q(entregado=False),  Q(disposicion=tribunal), Q(placa_patente__icontains=buscar) | Q(numero_de_parte__icontains=buscar ) )

        context['disposicion'] = tribunal
        context['cantidad'] = cantidad_vehiculos
        context['vehiculos'] = vehiculos

        return context

            
@method_decorator(login_required, name='dispatch')
class VehiculosEntregados(ListView):
    model = Vehiculo
    template_name = 'pages/filtrados/vehiculos_entregados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        vehiculos = Vehiculo.objects.filter(entregado=True).order_by('-id')
        cantidad_vehiculos_entregados = vehiculos.count()
        buscar = self.request.GET.get('buscar')

        if buscar:
            vehiculos = Vehiculo.objects.filter( Q(entregado=True), Q(placa_patente__icontains=buscar) | Q(numero_de_parte__icontains=buscar ) )

        context['vehiculos'] = vehiculos
        context['cantidad'] = cantidad_vehiculos_entregados

        return context


@method_decorator(login_required, name='dispatch')
class DetalleVehiculo(ListView):
    model = Vehiculo
    model = Propietario_vehiculo
    model = Entrega_vehiculo
    template_name = 'pages/detalle/detalle_vehiculo.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        detalle_vehiculo = get_object_or_404(Vehiculo, id=self.kwargs['id'])
        propietario_vehiculo = Propietario_vehiculo.objects.filter(vehiculo=detalle_vehiculo).first()
        entrega_vehiculo = Entrega_vehiculo.objects.filter(vehiculo=detalle_vehiculo).first()

        try:
            context['vehiculo'] = detalle_vehiculo
            context['propietario'] = propietario_vehiculo
            context['entrega'] = entrega_vehiculo

        except Propietario_vehiculo.DoesNotExist:
            context['vehiculo'] = detalle_vehiculo
            context['propietario'] = None
            context['entrega'] = None

        return context


@method_decorator(login_required, name='dispatch')
class ModificarVehiculo(UpdateView):
    model = Vehiculo
    template_name = 'pages/modificacion/modificar_vehiculo.html'
    form_class = FormularioVehiculo
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, "Modificación del vehículo registrada con éxito!")
            return super().form_valid(form)
        
        except IntegrityError:
            messages.error(self.request, "La P.P.U. que deseas modificar ya se encuentra registrada" )
            return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('modificar_vehiculo', kwargs={'pk': self.object.pk})
    
    def form_invalid(self, form):
        messages.error(self.request, "La P.P.U. que deseas modificar ya se encuentra registrada" )
        return super().form_invalid(form)



@method_decorator(staff_member_required, name='dispatch')
class EliminarVehiculo(DeleteView):
    model = Vehiculo
    template_name = 'pages/eliminar/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('home')


        




    