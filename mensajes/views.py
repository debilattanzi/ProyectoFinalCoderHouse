
from usuarios.views import *
from mensajes.forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def mensajeformulario(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            fecha = informacion["fecha"]
            mensaje = informacion["mensaje"]
            enviar_a = informacion["enviar_a"]
            destinatario = informacion["destinatario"]
            chat = Mensajes(fecha=fecha, mensaje=mensaje, destinatario=destinatario, enviar_a=enviar_a)
            chat.save()
        return render(request, 'inicio.html', {"mensaje": f"Mensaje enviado correctamente", "imagen": obteneravatar(request)})
    else:
        formulario = MensajeForm()
    return render(request, "mensajeformulario.html", {"form": formulario, "imagen": obteneravatar(request)})

@login_required
def mostrarmensaje(request):
    usuario=request.user
    mens = Mensajes.objects.filter(enviar_a=usuario)
    return render(request, "mostrarmensaje.html", {"mens": mens, "imagen": obteneravatar(request)})


def respondermensaje(request,id):
    mens = Mensajes.objects.filter(id=id)

