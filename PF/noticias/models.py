from django.db import models

class Noticia(models.Model):
    nombre=models.CharField(max_length=255)
    titulo=models.CharField(max_length=255)
    fecha=models.DateField(auto_created=True)
