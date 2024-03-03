from django.db import models
import myapp.paths as path

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



# MODELOS CON CONVECCIONES MÁS AVANZADAS Y SUBCLASE.
class Autor(models.Model):
    model = 'AutorDeAlgunLibro'# ESTO LITERALMENTE NO HACE NADA. 

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre

# ESTO ES UNA CLASE BASE POR QUE TIENE abstract = True
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()

    class Meta:
        abstract = True # ESTO ESTABLECE QUE EL MODELO SEA UNA CLASE BASE
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['id']# ORDENA LOS DATOS SEGUN EL ID

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class LibroDigital(Libro):
    formato = models.CharField(max_length=50)
    tamano = models.CharField(max_length=50)
    url_descarga = models.URLField()
    autor_adicional = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros_digitales')

    class Meta:
        verbose_name = "Libro Digital"
        verbose_name_plural = "Libros Digitales"

# IMAGES ---------------------------------------------
class camareografo(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    class Meta:
        verbose_name = "El Camareografo"
        verbose_name_plural = "Los Camareografos"
        ordering = ['-id']

    def max_id_fotografico(self):
        detalle = self.RegistroFotografico_set.all().order_by('id').last()
        return detalle.id if detalle else 0
    
    def fotos_fotograficos(self):
        detalle = self.RegistroFotografico_set.all().order_by('id')
        return detalle


class fotografico(models.Model):
    class Meta:
        abstract = True
        ordering = ['-id']

    foto_descripcion=models.TextField(blank=True,null=True)
    foto_orientacion=models.CharField(
        max_length=255,
        null=True, blank=True,
        default='-')

    def __str__(self):
        return f"La descripcion es: {self.foto_descripcion}"

class RegistroFotografico(fotografico):
    model = 'RegistroFotografico'
    class Meta:
        verbose_name = "Foto - Registro fotografico"
        verbose_name_plural = "Fotos - Registros fotograficos"
        ordering = ['-id']
    
    id_camareografo = models.ForeignKey(camareografo, on_delete=models.CASCADE)
    foto_imagen = models.ImageField(upload_to=path.get_registro_fotografico_path, blank=True, null=True, max_length = 500)