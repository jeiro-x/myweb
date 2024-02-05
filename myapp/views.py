from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonaForm

# Create your views here.
def mi_vista(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()  # Guarda la instancia del modelo en la base de datos
			return render(request, 'inicio.html', {'form': form})
	else:
		form = PersonaForm()
	return render(request, 'inicio.html', {'form': form})



# VISTAS BASADAS EN CLASES
# gestion_personas/views.py
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Persona
from .forms import PersonaForm
from django.urls import reverse_lazy

class CrearPersonaView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'inicio.html'
    success_url = reverse_lazy('lista_personas')

class ListaPersonasView(ListView):
    model = Persona
    template_name = 'gestion_personas.html'
    context_object_name = 'personas'
