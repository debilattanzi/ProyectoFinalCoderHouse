from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from usuarios.forms import RegistroUsuarioForm, UserEditForm, AvatarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from usuarios.models import Avatar


# Create your views here.


def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, 'inicio.html', {"mensaje": f"Usuario: {username} creado correctamente", "imagen":obteneravatar(request)})
        else:
            return render(request, 'registro.html', {"form": form, "mensaje": "Error al registrar el usuario", "imagen":obteneravatar(request)})
    else:
        form = RegistroUsuarioForm
    return render(request, 'registro.html', {"form": form, "imagen":obteneravatar(request)})


def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu = form.cleaned_data.get("username")
            cont = form.cleaned_data.get("password")

            usuario = authenticate(username=usu, password=cont)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'inicio.html', {"imagen":obteneravatar(request)})
            else:
                return render(request, 'login.html', {"mensaje": "Usuario y/o Contraseña incorrecta", "form": form, "imagen":obteneravatar(request)})
        else:
            return render(request, 'login.html', {"mensaje": "Usuario y/o Contraseña incorrecta", "form": form, "imagen":obteneravatar(request)})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


@login_required
def editarusuario(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje": "Usuario editado correctamente", "imagen":obteneravatar(request)})
        else:
            return render(request, "editarusuario.html",
                          {"form": form, "nombreusuario": usuario.username, "mensaje": "Error al editar usuario", "imagen":obteneravatar(request)})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "editarusuario.html", {"form": form, "nombreusuario": usuario.username, "imagen":obteneravatar(request)})

@login_required
def obteneravatar(request):
    lista = Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
       imagen=lista[0].imagen.url
    else:
        imagen="/media/avatar/imagenpordefecto.png"
    return imagen

@login_required
def agregaravatar(request):
    if request.method == "POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo = Avatar.objects.filter(user=request.user)
            if len(avatarViejo) != 0:
                avatarViejo[0].delete()
            avatar = Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "inicio.html", {"mensaje": "Avatar agregado correctamente", "imagen":obteneravatar(request)})
        else:
            return render(request, "agregaravatar.html", {"formulario": form, "usuario": request.user, "imagen":obteneravatar(request)})
    else:
        form = AvatarForm()
        return render(request, "agregaravatar.html", {"formulario": form, "usuario": request.user, "imagen":obteneravatar(request)})




















