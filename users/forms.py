from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
import re
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electronico',
                    'required': True,
                    'pattern': '^[0-9]{5}[A-Za-z]{2}[0-9]{3}@utez\.edu\.mx$',
                    'title': 'Debe ser un correo institucional, ejemplo: 20203tn072@utez.edu.mx',
                    'maxlength': 150, 
                }
            ),
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre completo',
                    'required': True,
                    'maxlength': 100,
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellidos',
                    'required': True,
                    'maxlength': 100,
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula',
                    'required': True,
                    'pattern': '^[0-9]{5}[A-Za-z]{2}[0-9]{3}$',
                    'title': 'Debe ser una matricula de la UTEZ, ejemplo: 20203tn072',
                    'maxlength': 20,
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'required': True,
                    'pattern': '^[0-9]{10}$',
                    'title': 'Debe ser un número de 10 dígitos',
                    'maxlength': 15,
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                    'pattern': '^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                    'title': 'Debe contener al menos 8 caracteres, una mayúscula, un número y un carácter especial'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirmar Contraseña',
                    'required': True,
                }
            ),

        }

    def clean(self):
        cleaned_data = super().clean()
        
        email = cleaned_data.get('email')
        if not re.match(r'^[0-9]{5}[A-Za-z]{2}[0-9]{3}@utez\.edu\.mx$', email):
            raise ValidationError("El correo electrónico debe ser del dominio @utez.edu.mx.")
        
        control_number = cleaned_data.get('control_number')
        if not re.match(r'^[0-9]{5}[A-Za-z]{2}[0-9]{3}$', control_number):
            raise ValidationError("La matrícula debe ser de la utez con 10 caracteres.")
        
        tel = cleaned_data.get('tel')
        if not re.match(r'^[0-9]{10}$', tel):
            raise ValidationError("El teléfono debe tener exactamente 10 dígitos.")
        
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password1):
            raise ValidationError("La contraseña debe tener al menos 8 caracteres, 1 mayúscula, 1 número y 1 carácter especial (!, #, $, %, & o ?).")
        
        return cleaned_data
    


class CustomUserLoginForm(AuthenticationForm):
    email = forms.CharField(label="Correo electrónico", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
    fields = ['username', 'password']

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico o Usuario',
            }
        )
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'pattern': '^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                'title': 'Debe contener al menos 8 caracteres, una mayúscula, un número y un carácter especial (!, #, $, %, & o ?)'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
               raise forms.ValidationError("Usuario o contraseña incorrectos.")
            return cleaned_data

