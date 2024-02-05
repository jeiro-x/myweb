from django.urls import path
from . import views

urlpatterns = [
	path('', views.mi_vista, name='n_mi_vista'),

	# URL DE UNA VISTA BASADA EN CLASES
	path('crear_persona/', views.CrearPersonaView.as_view(), name='crear_persona'),
	path('lista_personas/', views.ListaPersonasView.as_view(), name='lista_personas'),
]