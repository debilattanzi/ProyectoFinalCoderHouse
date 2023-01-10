from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


# Create your models here.


class Mensajes(models.Model):
    enviar_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enviar', blank=True, default=None)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recibir', blank=True, default=None)
    mensaje = models.CharField(max_length=5000)
    fecha = models.DateField()

    def __str__(self):
        return self.mensaje + " " + self.fecha
