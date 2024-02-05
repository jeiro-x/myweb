from django.db import models

# Create your models here.
# class RegistroExcavacionDelimitacion(models.Model):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     class Meta:
#         verbose_name = "Excavacion Delimitacion - Registro"
#         verbose_name_plural = "Excavacion Delimitacion - Registro"
#         ordering = ['-id']

#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     #Datos generales
#     proyecto_nombre = models.CharField(max_length=255,null=True, blank=True)
#     nombre_bien_arqueologico = models.CharField(max_length=255,null=True, blank=True)
#     otros_nombres = models.CharField(max_length=255,null=True, blank=True)
#     is_active = models.BooleanField(default=True, null=True)
#     is_valid = models.BooleanField(default=True, null=True)
#     fecha = models.DateField(auto_now_add=False, blank=True, null=True)

#     validado = models.BooleanField(default=False)

#     # Auditoria
#     activo = models.BooleanField(default=True, null=True)
#     eliminado_fecha = models.DateField(auto_now=False, blank=True, null=True)

#     #METODOS DE INSTANCIA
#     def unidades(self):
#         detalle = self.unidadexcavacion_set.all()
#         return detalle
    
#     def capas(self):
#         detalle = self.capaexcavacion_set.all()
#         return detalle

#     def registrofotografico(self):
#         detalle = self.registrofotograficoexcavacion_set.all().reverse()
#         return detalle

#     def max_id_fotografico(self):
#         detalle = self.registrofotograficoexcavacion_set.all().order_by('id').last()
#         return detalle.id if detalle else 0

#     def registrografico(self):
#         detalle = self.registrograficoexcavacion_set.all().reverse()
#         return detalle

#     def max_id_grafico(self):
#         detalle = self.registrograficoexcavacion_set.all().order_by('id').last()
#         return detalle.id if detalle else 0
    
#     def fotos_graficos(self):
#         detalle = self.registrograficoexcavacion_set.all().order_by('id')
#         return detalle
    
#     def fotos_fotograficos(self):
#         detalle = self.registrofotograficoexcavacion_set.all().order_by('id')
#         return detalle


# MIS MODELO
class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)

    # METODOS DE INSTANCIA
    def __str__(self):
    	return f"{self.id} - {self.ciudad} - {self.calle} - De dirección"


class Persona(models.Model):
    # Campos del modelo
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()
    
    #METODOS DE INSTANCIA
    def __str__(self):
        return self.nombre

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def direcciones(self):
        direcciones_asociadas = self.direccion_set.all()
        return direcciones_asociadas


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    departamento = models.CharField(max_length=50)

    #METODOS DE INSTANCIA
    def __str__(self):
        return f"{self.nombre} ({self.departamento})"

    def calcular_bonus(self, porcentaje):
        bonus = self.salario * (porcentaje / 100)
        return f"¡{self.nombre} ha ganado un bonus de {bonus:.2f} porcentajes!"

    def promover(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        self.save()
        return f"{self.nombre} ha sido promovido al departamento de {nuevo_departamento}."

    def saludo_empleado(self):
    	return f"este hola es para la genta, saludos {self.nombre} tu id es {self.id}"

