from rest_framework import viewsets
from escola.models import Estudante,Curso
from escola.serializers import EstudanteSerializer,CursoSerializer

class EstudantesViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

