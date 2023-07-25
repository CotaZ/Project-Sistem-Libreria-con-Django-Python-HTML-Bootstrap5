from django.db import models
from django.core.validators import EmailValidator

class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True) #python -m pip install Pillow
    descripcion = models.TextField(verbose_name= "Descripción", null=True)
    archivo_pdf = models.FileField(upload_to='pdfs/', verbose_name='PDF del Libro', null=True) #pip install django-filebrowser
    
    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return "Título: " + self.titulo + " - Descripción: " + self.descripcion



    def eliminar(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        if self.imagen:
            self.imagen.storage.delete(self.imagen.name)
        if self.archivo_pdf:
            self.archivo_pdf.storage.delete(self.archivo_pdf.name)
        super().delete()

class UsuarioExterno(models.Model):
    NINGUNA = 'Ninguna'
    ESTUDIANTE = 'Estudiante'
    PROFESIONAL = 'Profesional'
    EDUCADOR = 'Educador'
    OPCIONES_PROFESION = (
        (NINGUNA, 'Ninguna'),
        (ESTUDIANTE, 'Estudiante'),
        (PROFESIONAL, 'Profesional'),
        (EDUCADOR, 'Educador'),
    )

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveIntegerField()
    profesion = models.CharField(max_length=20, choices=OPCIONES_PROFESION, default=NINGUNA)
    rut = models.CharField(max_length=12)
    email = models.EmailField()
    confirmacion_email = models.EmailField()
    
    contraseña = models.CharField(max_length=128)
    confirmacion_contraseña = models.CharField(max_length=128)
    pais = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
