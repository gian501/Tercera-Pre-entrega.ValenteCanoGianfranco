from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppE03.models import Curso
from AppE03.models import Profesor
from AppE03.models import Estudiante
from AppE03.models import Entregable
from AppE03.forms import CursoFormulario
from AppE03.forms import ProfesoresFormulario
from AppE03.forms import EstudiantesFormulario
from AppE03.forms import EntregableFormulario

# Create your views here.


def inicio(request):
    return render(request, "AppE03/inicio.html", )
    
def cursos(request):
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "AppE03/cursos.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = CursoFormulario()
        
    return render(request, 'AppE03/cursos.html',{"miFormulario": miFormulario})


def profesores(request):
    
    if request.method == "POST":
 
        miFormulario = ProfesoresFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"], profesion=informacion["profesion"])
            profesor.save()
        return render(request, "AppE03/profesores.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = ProfesoresFormulario()
        
    return render(request, 'AppE03/profesores.html',{"miFormulario": miFormulario})

def estudiantes(request):
    if request.method == "POST":
 
        miFormulario = EstudiantesFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            estudiante.save()
        return render(request, "AppE03/estudiantes.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = EstudiantesFormulario()

    return render(request, 'AppE03/estudiantes.html',{"miFormulario": miFormulario})


def entregables(request):
   
    if request.method == "POST":
 
        miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable (nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"], fechaEntrega=informacion["fechaEntrega"],entregado=informacion["entregado"])
            entregable.save()
        return render(request, "AppE03/entregables.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = EntregableFormulario()

    return render(request, 'AppE03/entregables.html',{"miFormulario": miFormulario})

def busquedaComision(request):
    return render(request, "AppE03/busquedaComision.html" )

def buscar(request):
    if request.GET['comision']:
        comision= request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "AppE03/resultadoBusqueda.html", {"cursos":cursos, "comision":comision})
    else:
        respuesta = "No enviaste datos"
    
    #return render(request, 'AppC/inicio.html',{"respuesta": respuesta})
    return HttpResponse(respuesta)