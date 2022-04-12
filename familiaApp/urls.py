"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 

from django.urls import include, path
from .views import SearchView, listado_familia
from familiaApp import views
from django.views.generic import TemplateView
from .views import FormularioView, SearchView
urlpatterns = [
    path("familiares/",listado_familia),
    
    path("",views.inicio),
    path("cursos",views.cursos,name="Cursos"),
    path("profesores",views.profesores),
    path("estudiantes",views.estudiantes),
    path("entregables",views.entregables),
    path("home",TemplateView.as_view(template_name="AppCoder/home.html"),name="home"),
    path("formulario",FormularioView.as_view(),name="formulario"),
    path("search",SearchView.as_view(),name="search"),


]