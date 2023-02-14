from django.shortcuts import render
from django.http import HttpResponse
'''
from AppC.models import Curso
from AppC.models import Profesor
from AppC.models import Estudiante
from AppC.models import Entregable
from AppC.forms import CursoFormulario
from AppC.forms import ProfesoresFormulario
from AppC.forms import EstudiantesFormulario
from AppC.forms import EntregableFormulario
'''
# Create your views here.


def inicio(request):
    
    return render(request, "AppC/inicio.html", )
    #return HttpResponse('Vista Inicio')

def cursos(request):
    '''
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "AppC/cursos.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = CursoFormulario()
        
    return render(request, 'AppC/cursos.html',{"miFormulario": miFormulario})
    '''
    return render(request, 'AppC/inicio.html')
    #return HttpResponse('Vista cursos')

def profesores(request):
    '''
    if request.method == "POST":
 
        miFormulario = ProfesoresFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],email = informacion["e-mail"], profesion = informacion['profesion'])
            profesor.save()
        return render(request, "AppC/profesores.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = ProfesoresFormulario()
        
    return render(request, 'AppC/profesores.html',{"miFormulario": miFormulario})
    '''
    return render(request, 'AppC/profesores.html')
    #return HttpResponse('Vista profesores')



def estudiantes(request):
    '''
    if request.method == "POST":
 
        miFormulario = EstudiantesFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email = informacion["e-mail"])
            estudiante.save()
        return render(request, "AppC/estudiantes.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = EstudiantesFormulario()

    return render(request, 'AppC/estudiantes.html',{"miFormulario": miFormulario})
    '''
    return render(request, 'AppC/estudiantes.html')
    #return HttpResponse('Vista estudiantes')

def entregables(request):
    '''
    if request.method == "POST":
 
        miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable (nombre=informacion["nombre"],apellido=informacion["apellido"],email = informacion["e-mail"], fechadeentrega=informacion["Fecha de entrega"],entregado = informacion["entregado"])
            entregable.save()
        return render(request, "AppC/entregables.html" ) #ubicacion a donde me lleva
    else:
        miFormulario = EntregableFormulario()

    return render(request, 'AppC/entregables.html',{"miFormulario": miFormulario})
    '''
    return render(request, 'AppC/entregables.html')
    #return HttpResponse('Vista entregables')
