from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonaForm, FotograficoForm
from .models import Persona, camareografo
from django.urls import reverse, reverse_lazy
# from . import views

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

# ESTOS 'django.views.generic' ES UN MODULO QUE CONTIENE CLASES
# from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# from .models import PersonaDetailFormRegistroElemetos

# POR EJEMPLO TemplateView ES UNA CLASE DE VISTA
class UltimaPersonaView(CreateView):
	# ESTOS SON ATRIBUTOS
	model = Persona
	form_class = PersonaForm
	template_name = 'analisis_persona.html'
	success_url = reverse_lazy('n_analisis')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# Obtener la última persona registrada
		ultima_persona = Persona.objects.latest('id')
		# Agregar nombre y apellido al contexto
		context['nombre'] = ultima_persona.nombre
		context['edad'] = ultima_persona.edad
		context['correo'] = ultima_persona.correo
		return context

	def form_valid(self, form):
		# Se ejecuta si el formulario es válido
		# Puedes realizar acciones adicionales aquí, como guardar datos adicionales
		self.object = form.save()

		print("Aqui estamos.----------------------------------------------")

		# Imprimir los datos del formulario
		cleaned_data = form.cleaned_data
		print("/////////")
		print(cleaned_data)
		for field, value in cleaned_data.items():
			print(f"{field}: {value}")

		return super().form_valid(form)

	def form_invalid(self, form):
		# Se ejecuta si el formulario no es válido
		# Puedes realizar acciones adicionales aquí, como mostrar mensajes de error personalizados
		print("Ourrio un Error ------")

		name = self.request.POST.get('nombre')
		print(name)


		# Imprimir los datos del formulario
		cleaned_data = form.cleaned_data
		print("/////////")
		print(cleaned_data)
		for field, value in cleaned_data.items():
			print(f"{field}: {value}")

		return super().form_invalid(form)

	# def get_absolute_url(self):
	# 	return reverse('n_analisis', kwargs={'pk': self.pk})

	# def get_success_url(self):
	# 	return reverse('n_analisis', args=[self.object.pk])


# VISTAS BASADAS EN CLASES
# gestion_personas/views.py
# from django.views.generic import ListView
# from django.urls import reverse_lazy

# class CrearPersonaView(CreateView):
#     model = Persona
#     form_class = PersonaForm
#     template_name = 'inicio.html'
#     success_url = reverse_lazy('lista_personas')

# class ListaPersonasView(ListView):
#     model = Persona
#     template_name = 'gestion_personas.html'
#     context_object_name = 'personas'


class fotografico_view(CreateView):
	# ESTOS SON ATRIBUTOS
	model = camareografo
	form_class = FotograficoForm
	template_name = 'fotografico.html'
	success_url = reverse_lazy('n_fotografico')

from django.template.loader import get_template
from xhtml2pdf import pisa
# from html2pdf import HTML2PDF
def exportar_pdf(request):
	# Obtener el template HTML
    template = get_template('mi_export_pdf.html')
    html = template.render()

   	# Crear un archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mi_archivo.pdf"'

    # Convertir HTML a PDF
    pisaStatus = pisa.CreatePDF(html, dest=response)

    # Si todo salió bien, devolver el PDF
    if pisaStatus.err:
        return HttpResponse('Hubo un error al generar el PDF')
    return response