import datetime
from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField(default=datetime.date.today)
    lugar = models.CharField(max_length=255, default='')
    conclusion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
