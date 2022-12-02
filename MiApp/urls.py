
from django.urls import path
from MiApp.views import *

urlpatterns = [
    path("curso/", curso, name="curso"),
    path("cursos/", cursos, name="cursos"),
    path("foro/", foro, name="foro"),
    path("registro/", registrate, name="registrate"),
    path("", inicio, name="inicio"),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),

]