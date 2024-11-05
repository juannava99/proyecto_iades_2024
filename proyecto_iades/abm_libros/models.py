from django.db import models

# Create your models here.

class Cursos(models.Model):

    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()
    