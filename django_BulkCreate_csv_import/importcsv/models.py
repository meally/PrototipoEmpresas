from django.db import models
from django.utils.timezone import now

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=150, null=False)
    cantidad = models.IntegerField(null=False)
    fecha_vencimiento = models.DateField(null=False)
    supermercado = models.CharField(max_length=150, null=False)
    direccion = models.TextField(blank=False, null=False)

    def __str__(self):
       return self.nombre
