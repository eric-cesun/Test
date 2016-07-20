from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Categoria(models.Model):
    categoria= models.CharField(max_length=120)
    descripcion=models.TextField()
    creada = models.DateTimeField(auto_now=False, auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.categoria

class Autor(models.Model):
     nombreCompleto= models.CharField(max_length=120)
     imagen=models.FileField(null=True,blank=True)
     correo=models.CharField(max_length=120, null=True,blank=True)
     bibliografia = models.TextField()
     nacionalidad=models.CharField(max_length=120, null=True,blank=True)
     actualizado = models.DateTimeField(auto_now=True, auto_now_add=False)
     creado = models.DateTimeField(auto_now=False, auto_now_add=True)
     def __str__(self):
         return self.nombreCompleto

class Libro(models.Model):
     titulo= models.CharField(max_length=120)
     imagen=models.FileField(null=True,blank=True)
     contenido = models.TextField()
     creado = models.DateTimeField(auto_now=False, auto_now_add=True)
     autor =models.ForeignKey(Autor,null=True,blank=True)
     categoria=models.ForeignKey(Categoria)
     def __str__(self):
         return self.titulo
