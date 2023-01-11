from django.shortcuts import render
from Blog.forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post
from usuarios.views import *
from usuarios.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def inicio(request):
    return render(request, "inicio.html", {"imagen": obteneravatar(request)})


@login_required
def crearpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            titulo = informacion["titulo"]
            receta = informacion["receta"]
            imagenPost = informacion["imagenPost"]
            chef = informacion["chef"]
            fecha = informacion["fecha"]
            post = Post(titulo=titulo, receta=receta, imagenPost=imagenPost, chef=chef, fecha=fecha)
            post.save()
            return render(request, "inicio.html",
                          {"mensaje": f"Post creado correctamente", "imagen": obteneravatar(request)})
    else:
        formulario = PostForm()
    return render(request, "crearpost.html", {"form": formulario, "imagen": obteneravatar(request)})


def mostrarpost(request):
    posteo = Post.objects.all()
    if len(posteo) != 0:
        return render(request, "mostrarpost.html", {"posteo": posteo, "imagen": obteneravatar(request)})
    else:
        return render(request, "mostrarpost.html",
                      {"mensaje": f"No se encontraron Post", "posteo": posteo, "imagen": obteneravatar(request)})



def mispost(request, chef):
    posteo = Post.objects.filter(chef=chef)
    if len(posteo) != 0:
        return render(request, "mispost.html", {"posteo": posteo, "imagen": obteneravatar(request)})
    else:
        return render(request, "mispost.html",
                      {"mensaje": f"No se encontraron Post", "posteo": posteo, "imagen": obteneravatar(request)})


@login_required
def borrarpost(request, titulo):
    posteo = Post.objects.get(titulo=titulo)
    posteo.delete()
    post = Post.objects.all()
    return render(request, "mispost.html",
                  {"mensaje": "Post eliminado correctamente", "post": post, "imagen": obteneravatar(request)})


@login_required
def editarpost(request, titulo):
    posteo = Post.objects.get(titulo=titulo)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            posteo.titulo = info["titulo"]
            posteo.receta = info["receta"]
            posteo.imagenPost = info["imagenPost"]
            posteo.chef = info["chef"]
            posteo.fecha = info["fecha"]
            posteo.save()
            post = Post.objects.all()
            return render(request, "mispost.html",
                          {"mensaje": "Post Editado", "post": post, "imagen": obteneravatar(request)})
    else:
        formulario = PostForm(
            initial={"titulo": posteo.titulo, "receta": posteo.receta, "imagenPost": posteo.imagenPost,
                     "chef": posteo.chef, "fecha": posteo.fecha})
    return render(request, "editarpost.html",
                  {"form": formulario, "posteo": posteo, "imagen": obteneravatar(request)})


def filtrarpost(request, titulo):
    posteo = Post.objects.get(titulo=titulo)
    return render(request, "filtrarpost.html", {"posteo": posteo, "imagen": obteneravatar(request)})


def acercademi(request):
    return render(request, "acercademi.html", {"imagen": obteneravatar(request)})
