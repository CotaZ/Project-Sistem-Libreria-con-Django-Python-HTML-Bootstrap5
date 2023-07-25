from django import forms
from .models import Libro, UsuarioExterno


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__' #Actualizara el formulario para incluir todos los campos

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioExterno
        fields = '__all__'