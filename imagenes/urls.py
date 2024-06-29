from django.urls import path
from .views import SubidaImagen

urlpatterns = [
   path('subida/', SubidaImagen.as_view(), name='subida_img' )
]