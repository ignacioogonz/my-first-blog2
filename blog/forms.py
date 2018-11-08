from django import forms
from blog.models import Mascota, Datos, Usuario

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields =[
            'nombre',
            'raza',
            'descripcion',
            'estado',

        ]

        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'descripcion': 'Descripcion',
            'estado': 'Estado',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'raza': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),

        }

class Datos_PersonalesForm(forms.ModelForm):
    class Meta:
        model = Datos

        fields =(
            'correo',
            'rut',
            'nombre',
            'fecha',
            'telefono',
        )


class RegistroForm(forms.Form):
    # variable o input que apareceran en la vista
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()

