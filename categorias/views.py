from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse
import json

#Agregar un producto
def registrar_categoria(request):
    #Primero checamos como llegamos a esta función
    if request.method == 'POST':
        #Llegamos aqui por el envio de un formulario
        form = categoriaForm(request.POST) #Genera un formulario lleno con info
        if form.is_valid():
            form.save()
            return redirect('json') #Redirige a la lista de categoria
    else:
        form = categoriaForm()
    return render(request, 'registrar.html', {'form':form})


#Devuelve el JSON
def lista_categorias(request):
    categoria = Categoria.objects.all()

    #Para enviar un JSON debemos escribir los datos 
    #En un diccionario usando llaves
    #Diccionario personalizado
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categoria
    ]

    return JsonResponse(data, safe=False)

def json_vista(request):
    return render(request, 'jsonc.html')


def agregar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nueva_categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso',
                'id': nueva_categoria.id
            },status=201)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            },status=400)
    return JsonResponse({
        'error': 'Método no permitido'
    },status=405)