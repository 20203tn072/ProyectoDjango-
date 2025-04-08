from django import forms
from .models import Producto


class productoForm(forms.ModelForm):
    class Meta:

        #Definir de que modelo se basa el formulario
        model = Producto

        #Definir que campos van a ser incluidos en el formulario
        fields = ['nombre', 'precio', 'imagen', 'categoria']

        #Definir como se deben de ver o que atributos tienen los campos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

        #Etiquetas personalizadas
        label = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen',
            'categoria': 'Categoria del producto'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre': {'requiered': 'El nombre es obligatorio'},
            'precio': {'requiered': 'El precio no puede estar vacio', 'invalid': 'Ingrese un numero valido'}
            
        }