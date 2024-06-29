from rest_framework.views import APIView
from .serializer import ImagenSerializer
from rest_framework.response import Response
from rest_framework import status

class SubidaImagen(APIView):
   def post(self, request):
      serializer = ImagenSerializer(data=request.data)
      if serializer.is_valid():
         img_url = serializer.validated_data['img_url']    # patito.png
         img_url.name = 'images/' + img_url.name   #images/patito.png
         imagen = serializer.save()

         #Obtener la URL completa de cloudinary
         img_url_full = imagen.img_url.url  #.url  www.cloudinary/minube/carpeta/patito.png
         imagen.img_url_full = img_url_full
         imagen.save()
         
         # Actualizamos nuestra respuesta de la URL 
         respuesta = ImagenSerializer(imagen)
         return Response(respuesta.data, status=status.HTTP_201_CREATED)
      
   # get all
   # put edite la imagen
   # delete
