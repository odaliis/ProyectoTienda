

from django import forms
from .models import Docente
from django.contrib.auth import authenticate, login

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields=['nombre', 'apellido', 'edad', 'email', 'sexo']




class DocenteFormBasico(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    email = forms.EmailField(label='correo',  max_length=25)


