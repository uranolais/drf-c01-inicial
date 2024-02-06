from rest_framework import viewsets
from escola.models import Estudante,Curso,Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer,MatriculaSerializer

class EstudantesViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer