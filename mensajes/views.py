from django.shortcuts import render
from usuarios.views import *
from mensajes.forms import *

def mensajeformulario(request):
    if request.method == 'POST':
        form = MensajesForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            tiempo = informacion["tiempo"]
            mensaje = informacion["mensaje"]
            chat = Mensajes(tiempo=tiempo, mensaje=mensaje)
            chat.save()
            return render(request, 'inicio.html', {"mensajes": f"Mensaje correcto", "imagen": obteneravatar(request)})
    else:
        formulario = MensajesForm()
    return render(request, 'mensajeformulario.html', {'form': formulario, "imagen": obteneravatar(request)})
