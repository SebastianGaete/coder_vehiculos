from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import User
from django.contrib.auth import get_user_model

def atributos(atributos=None):
    estilos = {'class':'form-control shadow-none border-1 mb-2 border-secondary'}
    if atributos != None:
        estilos.update(atributos)
    return estilos

class UserCreationFormModificated(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "codigo_funcionario", "email", "grado"]

        widgets = {
            'first_name': forms.TextInput(attrs=atributos({'placeholder':'Nombre'})),
            'last_name': forms.TextInput(attrs=atributos({'placeholder':'Apellidos'})),
            'codigo_funcionario': forms.TextInput(attrs=atributos({'placeholder':'000000-X'})),
            'email': forms.EmailInput(attrs=atributos({'placeholder':'nombre@gmail.com'})),
            'grado': forms.Select(attrs=atributos()),
        }

    def verificar_numero_placa(self):
        codigo_funcionario = self.cleaned_data.get('codigo_funcionario')
        if get_user_model().objects.filter(codigo_funcionario=codigo_funcionario).exists():
            raise forms.ValidationError("Este código de funcionario ya está en uso.")
        return codigo_funcionario
    
    def verificar_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Esta dirección de correo electrónico ya está en uso.")
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field == self.fields['first_name']:
                field.required = True
            if field == self.fields['last_name']:
                field.required = True

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]
