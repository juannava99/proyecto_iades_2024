from django.db import models

# Create your models here.

class Libros(models.Model):

    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()
    ISBN = models.IntegerField(unique=True)
    
    