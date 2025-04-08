from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from .forms import alumnoForm

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]

def agregar_alumno(request):
    form = alumnoForm()
    return render(request, 'avelino_abraham.html', {'form':form})
