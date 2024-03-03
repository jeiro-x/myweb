from django import forms
from .models import Persona, camareografo

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        # fields = ['nombre', 'apellido', 'edad', 'correo']  # Lista de campos que deseas incluir en el formulario
        fields='__all__'

class FotograficoForm(forms.ModelForm):
	class Meta:
		model = camareografo
		fields = '__all__'