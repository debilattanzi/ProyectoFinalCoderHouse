from django import forms
from ckeditor.fields import RichTextField

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=20)
    receta = forms.CharField(label="Receta")
    imagenPost = forms.ImageField()
    chef = forms.CharField(max_length=50)
    fecha = forms.DateField()
