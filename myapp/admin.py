from django.contrib import admin
from .models import Direccion, Persona, Empleado, Autor, LibroDigital, camareografo, RegistroFotografico
# Register your models here.


admin.site.register(Direccion)
admin.site.register(Persona)
admin.site.register(Empleado)

admin.site.register(Autor)
admin.site.register(LibroDigital)

admin.site.register(camareografo)
admin.site.register(RegistroFotografico)