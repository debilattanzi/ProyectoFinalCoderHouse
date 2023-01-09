from django.shortcuts import render
from usuarios.views import *
from mensajes.forms import *
from django.contrib.auth.decorators import login_required

@login_required
def mensajeformulario(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            tiempo = informacion["tiempo"]
            mensaje = informacion["mensaje"]
            chat = Mensajes(tiempo=tiempo, mensaje=mensaje)
            chat.save()
            return render(request, 'inicio.html', {"mensajes": f"Mensaje correcto", "imagen": obteneravatar(request)})
    else:
        formulario = MensajeForm()
    return render(request, "mensajeformulario.html", {"form": formulario, "imagen": obteneravatar(request)})


"""

def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mens = form.save(commit=False)
            mens.enviar = request.user
            mens.save()
            return render(request, 'inicio.html', {"mensaje": f"Mensaje correcto", "imagen": obteneravatar(request)})
    else:
        form = MensajeForm()
    return render(request, 'mensajeformulario.html', {'form': form, "imagen": obteneravatar(request)})
"""
