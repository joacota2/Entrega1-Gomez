from multiprocessing import context
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Curso,Estudiante,Profesor,Familiar
from .forms import CursoForms,EstudianteForms,ProfesorForms  




def listado_familia(request):
   
    template = loader.get_template('listado_familia.html')
    familiares=Familiar.objects.all()
    print(familiares)
    context = {
        'familiares': familiares,
    }
    return HttpResponse(template.render(context, request))



def inicio(request):
    return render(request, "AppCoder/home.html")
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
        
        
        response=CursoForms(request.POST)
        
        if response.is_valid:

            print(response)
            
            obj_response = response.cleaned_data

            nombre = obj_response["nombre"]
            camada = obj_response["camada"]
            print(f"CURSO:{nombre}")
            print(f"CAMADA:{camada}")
        
            obj_curso = Curso(nombre=obj_response.get("nombre"), camada=obj_response.get("camada"))
            obj_curso.save()


        context={
            "form":CursoForms()
        }

        return render(request,self.template_name,context)







          

class SearchView(TemplateView):
    template_name= "forms/search.html"

    def post(self,request):

        context={
            "elements":Curso.objects.filter(camada=request.POST.get("camada"))
        }

        return render(request,self.template_name,context)

#OPCION 1
"""class FormularioView(TemplateView):
    template_name="forms/index.html"
   
   
    def get(self,request):
        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }
        return render(request,self.template_name,context)

    def post(self,request):
        
        
        response=CursoForms(request.POST)
        
        if response.is_valid:

            print(response)
            
            obj_response = response.cleaned_data

            nombre = obj_response["nombre"]
            camada = obj_response["camada"]
            print(f"CURSO:{nombre}")
            print(f"CAMADA:{camada}")
        
            obj_curso = Curso(nombre=obj_response.get("nombre"), camada=obj_response.get("camada"))
            obj_curso.save()

        response1=EstudianteForms(request.POST)

        if response1.is_valid:
            obj_response1 = response1.cleaned_data

            obj_estudiante = Estudiante(nombre=obj_response1.get("nombre"),apellido=obj_response1.get("apellido"),email=obj_response1.get("email"))
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

        return render(request,self.template_name,context)"""






#OPCION 2
""" class FormularioView(TemplateView):
    template_name="forms/index.html"
   
   
    def get(self,request):
        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }
        return render(request,self.template_name,context)

    def post(self,request):
        
        
        response=CursoForms(request.POST)
        
        if response.is_valid:

            print(response)
            
            obj_response = response.cleaned_data

            nombre = obj_response["nombre"]
            camada = obj_response["camada"]
            print(f"CURSO:{nombre}")
            print(f"CAMADA:{camada}")
        
            obj_curso = Curso(nombre=obj_response.get("nombre"), camada=obj_response.get("camada"))
            obj_curso.save()

            response1=EstudianteForms(request.POST)
            if response1.is_valid:
                obj_response1 = response1.cleaned_data

                obj_estudiante = Estudiante(nombre=obj_response1.get("nombre"),apellido=obj_response1.get("apellido"),email=obj_response1.get("email"))
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

"""






#OPCION 3

""" class FormularioView(TemplateView):
    template_name="forms/index.html"
   
   
   def get(self,request):
        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }
        return render(request,self.template_name,context)

    def post(self,request):

        response=CursoForms(request.POST)
        response1=EstudianteForms(request.POST)
        response2=ProfesorForms(request.POST)
        if response.is_valid:
            obj_response = response.cleaned_data
            obj_curso = Curso(nombre=obj_response.get("nombre"), camada=obj_response.get("camada"))
            obj_curso.save()
            
            if response1.is_valid:
                obj_response1 = response1.cleaned_data
                obj_estudiante = Estudiante(nombre=obj_response1.get("nombre"),apellido=obj_response1.get("apellido"),email=obj_response1.get("email"))
                obj_estudiante.save()
                
                if response2.is_valid:
                    obj_response2 = response2.cleaned_data
                    obj_profesor = Profesor(nombre=obj_response2.get("nombre"), apellido=obj_response2.get("apellido"),email=obj_response2.get("email"),profesion=obj_response2.get("profesion"))
                    obj_profesor.save()
        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }

        return render(request,self.template_name, context)"""

 



 