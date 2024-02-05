from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        # fields = ['nombre', 'apellido', 'edad', 'correo']  # Lista de campos que deseas incluir en el formulario
        fields='__all__'
