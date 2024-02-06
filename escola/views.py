from rest_framework import viewsets, generics
from escola.models import Estudante,Curso,Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer

class EstudantesViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

# localhost:8000/estudante/1/matriculas
    
class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']) #Primary Key
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

# localhost:8000/curso/1/matriculas
class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk']) #Primary Key
        return queryset
    serializer_class = ListaMatriculasCursoSerializer