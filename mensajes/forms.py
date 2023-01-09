from django import forms

from mensajes.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
class MensajesForm(forms.Form):
    recibir = forms.ModelChoiceField(User.objects.all())
    mensaje = forms.CharField(max_length=5000)
"""

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensajes
        fields = ['recibir', 'mensaje', 'enviar', 'tiempo']