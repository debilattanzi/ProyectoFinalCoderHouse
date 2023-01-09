"""Proyecto_final_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Blog.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crearpost/', crearpost, name="crearpost"),
    path('mostrarpost/', mostrarpost, name="mostrarpost"),
    path('mispost/<chef>', mispost, name="mispost"),
    path('borrarpost/<titulo>', borrarpost, name="borrarpost"),
    path('editarpost/<titulo>', editarpost, name="editarpost"),
    path('filtrarpost/<titulo>', filtrarpost, name="filtrarpost"),
    path('acercademi/', acercademi, name="acercademi")

]
