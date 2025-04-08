from django.urls import path
from .views import *

urlpatterns = [
    path('registrar/', registrar_categoria, name='registrar'),
    path('api/get/', lista_categorias, name='lista'),
    path('json/', json_vista, name='json'),
    path('api/post/', agregar_categoria, name='POST')
]