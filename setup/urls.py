from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewset, CursosViewset, MatriculasViewset, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewset, basename='Alunos')
router.register('cursos', CursosViewset, basename='Cursos')
router.register('matriculas', MatriculasViewset, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
