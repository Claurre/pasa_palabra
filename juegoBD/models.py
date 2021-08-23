from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto = models.TextField ( verbose_name='Definición' ) 
    categoria = models.CharField ( verbose_name='categoía de la pregunta' , max_length=30) 
    letra = models.CharField ( max_length=1 , verbose_name='letra en el rosco') 
    respuesta = models.CharField ( verbose_name='respuesta' , max_length=60)

    def __str__(self):
        return self.texto 

class Rosco_pregunta(models.Model):
    letra_rosco = models.CharField(max_length=1)
    contestada = models.BooleanField(default=False)
    contestada_correcta = models.BooleanField(default=False)
