from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=20)
    receta = RichTextField()
    imagenPost = models.ImageField(upload_to='posteo', blank=True)
    chef = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo
