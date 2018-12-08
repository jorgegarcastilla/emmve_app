from django.db import models

# Create your models here.

class Poblacion(models.Model):

	nombre = models.CharField(max_length=50,verbose_name='Nombre')
	codigoPostal = models.CharField(max_length=5,verbose_name='C.P')
	provincia = models.CharField(max_length=25,verbose_name='Provincia')
	comunidadAutonoma = models.CharField(max_length=30,verbose_name='C.A')
	avatar = models.ImageField(verbose_name='Imagen', upload_to="poblaciones")
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

	class Meta:
		verbose_name = "Población"
		verbose_name_plural = "Poblaciones"
		ordering = ["comunidadAutonoma","provincia","nombre","codigoPostal"]
		
	def __str__(self):
		return self.nombre