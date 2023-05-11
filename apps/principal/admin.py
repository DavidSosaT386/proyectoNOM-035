from django.contrib import admin
from .models import Empleado, encuesta, respuesta, resultado
from django.utils.html import format_html

class encuestaAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['empleado', 'contestado']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
  
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)

class empleadodis(admin.ModelAdmin):
    list_display= ['id','pregunta','eleccion','empleado']
class empleados(admin.ModelAdmin):
    list_display= ['RPE','apellidos','nombre','centro_trabajo','foto_perfil']
    search_fields = ['RPE','nombre','apellidos']  
    list_editable = ['foto_perfil']
    list_filter = ['centro_trabajo']
    #def foto(self, obj):
     #   return format_html('<img src= {} width=50px height= 50px />', obj.foto_perfil.url )

admin.site.register(Empleado,empleados)
admin.site.register(resultado,encuestaAdmin)
admin.site.register(encuesta)

admin.site.register(respuesta,empleadodis)