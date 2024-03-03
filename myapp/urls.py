from django.urls import path
from . import views
from .views import UltimaPersonaView, fotografico_view

urlpatterns = [
	path('', views.mi_vista, name='n_mi_vista'),

	# URL DE UNA VISTA BASADA EN CLASES
	# path('crear_persona/', views.CrearPersonaView.as_view(), name='crear_persona'),
	# path('lista_personas/', views.ListaPersonasView.as_view(), name='lista_personas'),
	# LLAMAMOS A UNA CLASE DE TIPO VISTAT
	path('analisis', UltimaPersonaView.as_view(), name='n_analisis'),

	path('fotografico', fotografico_view.as_view(), name='n_fotografico'),

	path('exportar_pdf', views.exportar_pdf,  name='n_exportar_pdf'),
]