from django.urls import path
from .views import *

urlpatterns = [
    path('ver/', ver_productos, name='ver'),
    path('agregar/', agregar_producto, name='agregar'),
    path('api/get/', lista_productos, name='lista'),
    path('json/', json_view, name='jason'),
    path('api/post/', registrar_producto, name='POST'),
]