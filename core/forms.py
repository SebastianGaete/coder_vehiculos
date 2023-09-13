from .models import Vehiculo, Propietario_vehiculo, Entrega_vehiculo
from django import forms

def atributos_custom(atributos=None):
    atributos_bases ={
        'class':'form-control shadow-none border-1 mb-2 border-secondary',
    }
    if atributos:
        atributos_bases.update(atributos)
    return atributos_bases


class FormularioVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"
        exclude = ['entregado', 'registro_propietario', 'funcionario_receptor', 'funcionario_entrega' ]

        widgets = {
            'tipo': forms.Select(attrs= atributos_custom()),
            'marca': forms.TextInput(attrs= atributos_custom( {'placeholder':'Marca*'} )),
            'modelo': forms.TextInput(attrs= atributos_custom({'placeholder':'Modelo*'})),
            'placa_patente': forms.TextInput(attrs= atributos_custom({'minlength':'6', 'placeholder':'KKSS11*'})),
            'año': forms.TextInput(attrs= atributos_custom({'placeholder':'2000*'})),
            'color': forms.TextInput(attrs= atributos_custom({'placeholder':'Color*'})),
            'imagen': forms.FileInput(attrs=atributos_custom()),
            'motivo': forms.Select(attrs=atributos_custom() ),
            'disposicion': forms.Select(attrs=atributos_custom()),
            'fecha_ingreso': forms.DateInput(attrs= atributos_custom({'type':'datetime-local'})),
            'numero_de_parte': forms.NumberInput(attrs= atributos_custom({'placeholder':'Nro. de parte'})),
            'numero_de_oficio': forms.NumberInput(attrs= atributos_custom({'placeholder':'Nro. de oficio'})),
            'acta_entrega': forms.Select(attrs= atributos_custom()),
            'observaciones': forms.Textarea(attrs= atributos_custom({'placeholder':'Llena este campo si es necesario dejar en claro algún tipo de información.'})),
        }
    

class FormularioPropietarioVehiculo(forms.ModelForm):
    class Meta:
        model = Propietario_vehiculo
        fields = "__all__"
        exclude = ['vehiculo']

        widgets = {
                'nombre': forms.TextInput(attrs= atributos_custom({'placeholder':'Nombre del propietario*'} )),
                'apellidos': forms.TextInput(attrs= atributos_custom( {'placeholder':'Apellidos del propietario*'} )),
                'rut': forms.TextInput(attrs= atributos_custom({'minlength':'9', 'placeholder':'22000333-1*'})),
                'telefono': forms.TextInput(attrs= atributos_custom({'minlength':'10', 'placeholder':'9 00110011'})),
                'direccion': forms.TextInput(attrs= atributos_custom({'placeholder':'Dirección'})),
                'comuna': forms.TextInput(attrs= atributos_custom({'placeholder':'Comuna'})),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field == self.fields['telefono'] or field == self.fields['direccion'] or field == self.fields['comuna'] :
                field.required = False
            


class FormularioEntregaVehiculo(forms.ModelForm):
    class Meta:
        model = Entrega_vehiculo
        fields = "__all__"
        exclude = ['funcionario', 'vehiculo']

        widgets = {
                'numero_de_oficio': forms.NumberInput(attrs= atributos_custom({'placeholder':'Número de oficio*'} )),
                'vehiculo': forms.Select(attrs=atributos_custom()),
                'nombre': forms.TextInput(attrs= atributos_custom( {'placeholder':'Nombre persona que retira*'} )),
                'apellidos': forms.TextInput(attrs= atributos_custom({'placeholder':'Apellidos persona que retira*'})),
                'rut': forms.TextInput(attrs= atributos_custom({'minlength':'9', 'placeholder':'22000333-1*'})),
                'telefono': forms.TextInput(attrs= atributos_custom({'minlength':'10','placeholder':'9 00110011*'})),
                'observaciones': forms.Textarea(attrs= atributos_custom({'placeholder':'Llena este campo si es necesario dejar en claro algún tipo de información.'})),
            }