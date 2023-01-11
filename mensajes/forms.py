from django import forms

from mensajes.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensajes
        fields = ['remitente', 'mensaje', 'enviar_a', 'fecha']
