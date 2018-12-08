from django.db import models
""" from registration.models import Persona
from django.core.validators import MinValueValidator,MaxValueValidator

class Docente(Persona):

    #Atributos para el caso de docente
    link = models.URLField(null=True,blank=True,verbose_name='Dirección WEB')
    jornada = models.DecimalField(default=100.00,validators=[MinValueValidator(0),MaxValueValidator(100,0)],max_digits=5, decimal_places=2,verbose_name='Jornada')	
    rolDirector = models.BooleanField(null=True,verbose_name='Director')
    rolJefatura = models.BooleanField(null=True,verbose_name='Jefatura')


    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        ordering = ["nombre","primerApellido","segundoApellido"]

    def __str__(self):
        return '{} {} {}'.format(str(self.nombre),str(self.primerApellido),self.segundoApellido) """