from django import forms
from .models import respuesta, Empleado


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = respuesta
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
     class Meta:
         model = Empleado
         fields = ['RPE', 'nombre', 'apellidos', 'centro_trabajo']
         widgets = {
            'RPE': forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 70px;'}),
        }