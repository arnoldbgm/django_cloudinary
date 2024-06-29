from rest_framework import serializers
from .models import Imagen   # Es importar el modelo Imagen

class ImagenSerializer(serializers.ModelSerializer):

   # Deserializar
   # Convertir a json
   # Validaciones 

   img_url_full = serializers.CharField(source = 'img_url.url', read_only=True)

   class Meta:
      model = Imagen
      fields = ['id', 'nombre', 'img_url', 'img_url_full']
      # __all__