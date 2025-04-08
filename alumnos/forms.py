from django import forms
from .models import Alumno


class alumnoForm(forms.ModelForm):
    class Meta:

        #Definir de que modelo se basa el formulario
        model = Alumno

        #Definir que campos van a ser incluidos en el formulario
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        #Definir como se deben de ver o que atributos tienen los campos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellidos'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electronico'
                }
            )
        }

        #Etiquetas personalizadas
        label = {
            'nombre': 'Nombre del Alumno',
            'apellido': 'Apellidos',
            'edad': 'Edad',
            'matricula': 'Matricula',
            'correo': 'Correo Electronico'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre': {'requiered': 'El nombre es obligatorio'},
            'apellido': {'requiered': 'El apellido es obligatorio'},
            'edad': {'requiered': 'La edad es obligatoria'},
            'matricula': {'requiered': 'La matricula es obligatoria'},
            'correo': {'requiered': 'El correo es obligatorio'},
            
        }