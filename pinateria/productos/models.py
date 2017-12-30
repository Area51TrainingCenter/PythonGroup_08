from django.db import models


class Producto(models.Model):
    personaje = models.CharField(
        max_length=40,
        blank=False,
        null=False
    )

    nombre_comercial = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    precio = models.DecimalField(
        max_digits=15,
        decimal_places=5,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.personaje
