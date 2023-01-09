from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


# Create your models here.



class Mensajes(models.Model):
    enviar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enviar')
    recibir = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recibir')
    mensaje = models.CharField(max_length=5000)
    tiempo = models.DateField()

    def __str__(self):
        return self.mensaje + " " + self.tiempo
