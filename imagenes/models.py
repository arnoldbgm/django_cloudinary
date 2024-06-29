from django.db import models

# Create your models here.
# Dentro de los models siempre va ir las tablas

class Imagen(models.Model):
   nombre = models.CharField(max_length=100)
   img_url = models.ImageField(upload_to='images/', blank=True, null=True)
   img_url_full = models.URLField(blank= True, null= True)


# Debemos de crear un serializador en un archivo externo