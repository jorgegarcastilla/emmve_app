from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=200,default='', verbose_name='Título')
    # Todos los campos de ckEditor que quieras poder customizar algun atributo via css, en este caso para hacerlo adaptativo, 
    # tiene que tener este nombre content, ya que la clase tiene id_content como id.
    content = RichTextField(verbose_name='Descripción') 
    image = models.ImageField(verbose_name='Imagen', upload_to="noticias")
    link = models.URLField(null=True,blank=True,verbose_name='Dirección WEB')
    activa =  models.BooleanField(default=True,verbose_name='Activa')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-created','titulo']
    def __str__(self):
        return self.titulo
