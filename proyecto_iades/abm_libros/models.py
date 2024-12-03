from django.db import models

# Create your models here.

class Libros(models.Model):

    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    isbn = models.CharField(max_length=13,unique=True)
    