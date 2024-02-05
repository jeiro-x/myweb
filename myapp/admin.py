from django.contrib import admin
from .models import Direccion, Persona, Empleado
# Register your models here.


admin.site.register(Direccion)
admin.site.register(Persona)
admin.site.register(Empleado)