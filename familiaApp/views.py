import imp
from multiprocessing import context
from django.shortcuts import render
from django.template import loader
from .models import Familiar
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Curso
from .models import Estudiante
from .models import Profesor
from .forms import CursoForms
from .forms import EstudianteForms
from .forms import ProfesorForms

# Create your views here.


def listado_familia(request):
   
    template = loader.get_template('listado_familia.html')
    familiares=Familiar.objects.all()
    print(familiares)
    context = {
        'familiares': familiares,
    }
    return HttpResponse(template.render(context, request))

"""def inicio(request):
    return HttpResponse("vista inicio")
def cursos(request):
    return HttpResponse("vista cursos")
def profesores(request):
    return HttpResponse("vista profesores")
def estudiantes(request):
    return HttpResponse("vista estudiantes")
def entregables(request):
    return HttpResponse("vista entregables")"""


def inicio(request):
    return render(request, "AppCoder/inicio.html")
def cursos(request):
    return render(request, "AppCoder/cursos.html")
def profesores(request):
    return render(request, "AppCoder/profesores.html")
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
def entregables(request):
    return render(request, "AppCoder/entregables.html")
def cursoFormulario(request):
    return render(request, "AppCoder/cursoFormulario.html")


class FormularioView(TemplateView):
    template_name="forms/index.html"
    def get(self,request):
        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }
        return render(request,self.template_name,context)

    def post(self,request):
        """nombre=request.POST["nombre"]
        camada=request.POST["camada"]
        apellido=request.POST["apellido"]
        email=request.POST["email"]
        profesion=request.POST["profesion"]
        

        print(f"CURSO:{nombre}")
        print(f"CAMADA:{camada}")

        obj_curso = Curso(nombre=nombre, camada=camada)
        obj_curso.save()
        
        obj_estudiante = Estudiante(nombre=nombre, apellido=apellido,email=email)
        obj_estudiante.save()

        obj_profesor = Profesor(nombre=nombre, apellido=apellido,email=email,profesion=profesion)
        obj_profesor.save()"""

        response=CursoForms(request.POST)
        if response.is_valid:
            obj_response=response.cleaned_data
            obj_curso = Curso(nombre=obj_response.get("nombre"), camada=obj_response.get("camada"))
        obj_curso.save()

        response1=EstudianteForms(request.POST)
        if response1.is_valid:
            obj_response1=response1.cleaned_data
            obj_estudiante = Estudiante(nombre=obj_response1.get("nombre"), apellido=obj_response1.get("apellido"),email=obj_response1.get("email"))
        obj_estudiante.save()
       
        response2=ProfesorForms(request.POST)
        if response2.is_valid:
            obj_response2=response2.cleaned_data
            obj_profesor = Profesor(nombre=obj_response2.get("nombre"), apellido=obj_response2.get("apellido"),email=obj_response2.get("email"),profesion=obj_response2.get("profesion"))
        obj_profesor.save()

        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }

        return render(request,self.template_name,context)

class SearchView(TemplateView):
    template_name= "forms/search.html"

    def post(self,request):

        context={
            "elements":Curso.objects.filter(camada=request.POST.get("camada"))
        }

        return render(request,self.template_name,context)
