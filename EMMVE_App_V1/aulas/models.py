from django.db import models
from poblaciones.models import Poblacion
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Aula(models.Model):

	nombre = models.CharField(max_length=20,verbose_name='Nombre')
	superficie = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='Superficie')
	aforo = models.IntegerField(validators=[MinValueValidator(1)],verbose_name='Aforo máximo')
	poblacion = models.ForeignKey(Poblacion, null=True, blank = True,on_delete=models.SET_NULL)
	imagen = models.ImageField(verbose_name='Imagen', upload_to="aulas")
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

	class Meta:
		verbose_name = "Aula"
		verbose_name_plural = "Aulas"
		ordering = ["poblacion","nombre","superficie","aforo"]
		
	def __str__(self):
		return self.nombre