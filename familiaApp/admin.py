from django.contrib import admin

from .models import Familiar
from .models import *

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero','nacimiento')


admin.site.register(Familiar,FamiliarAdmin)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)