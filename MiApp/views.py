from django.shortcuts import render
from .models import Curso, Registrate
from django.http import HttpResponse

from MiApp.forms import CursoForm, RegistroForm

# Create your views here.
from django.shortcuts import render

def curso(request):

    curso1=Curso(nombre="Python",comision=34640)
    
    curso.save()
    cadena_Texto="Curso guardado: "+curso.nombre+" "+str(curso.comision)
    return HttpResponse(cadena_Texto)


def inicio(request):
    

    return render (request, "MiApp/inicio.html")


def cursos(request):
    return render (request, "MiApp/cursos.html")

def foro(request):
    return render (request, "MiApp/foro.html")

def registrate(request):

    if request.method=="POST":
        form=RegistroForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            tipoqa=informacion["tipoqa"]
            reg= Registrate(nombre=nombre, apellido=apellido, email=email, tipoqa=tipoqa)
            reg.save()
            return render (request, "MiApp/inicio.html", {"mensaje": "Registro finalizado"})
    else:
        formulario=RegistroForm()


    return render (request, "MiApp/registrate.html", {"form":formulario})


def cursoFormulario(request):

    if request.method=="POST":
        form=CursoForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombrecito=informacion["nombre"]
            comisioncita=informacion["comision"]

            curso1=Curso(nombre=nombrecito,comision=comisioncita)
            curso1.save()
            return render (request, "MiApp/inicio.html")
    else:
        formulario=CursoForm()


    return render(request, "MiApp/cursoFormulario.html", {"form":formulario})


def busquedaComision(request):
    return render(request, "MiApp/busquedaComision.html")


def buscar(request):

    if request.GET["comision"]:

        comision=request.GET["comision"]

        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"MiApp/resultadosBusqueda.html", {"cursos":cursos} )
    else:
        return render(request, "MiApp/busquedaComision.html", {"mensaje":"CHE! Ingresa una comision"})








