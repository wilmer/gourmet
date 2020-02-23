from django.contrib import admin
from menu import  models

# Register your models here.

class operadorAdmin(admin.ModelAdmin):
    search_fields = ['nombre_operador','usuario','password','tipo_operador']
    list_display = ('nombre_operador','usuario','password','tipo_operador')

class turnoAdmin(admin.ModelAdmin):
    search_fields = ['descripcion_turno']
    list_display = ('descripcion_turno',)

class equipoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_equipo', 'modelo', 'estado']
    list_display = ('nombre_equipo', 'modelo', 'estado')

class actividadAdmin(admin.ModelAdmin):
    search_fields = ['id_turno', 'id_operador', 'id_ayudante', 'id_equipo','fecha_actividad','nivel']
    list_display = ('id_turno', 'id_operador', 'id_ayudante', 'id_equipo','fecha_actividad','nivel')

class detalle_actividadAdmin(admin.ModelAdmin):
    search_fields = ['id_actividad', 'actividad', 'hora_inicio', 'hora_fin','codigo_operacion','descripcion_operacion','labor_origen','labor_destino','observaciones','tipo_material','labor_s','proyecto_s','fila_s','num_taladro_s','num_barras_s','longitud_s','inclinacion_s','num_broca_s','hr_diesel_inicial','hr_diesel_final','hr_electricidad_inicial_s','hr_electricidad_final_s']
    list_display = ('id_actividad', 'actividad', 'hora_inicio', 'hora_fin','codigo_operacion','descripcion_operacion','labor_origen','labor_destino','observaciones','tipo_material','labor_s','proyecto_s','fila_s','num_taladro_s','num_barras_s','longitud_s','inclinacion_s','num_broca_s','hr_diesel_inicial','hr_diesel_final','hr_electricidad_inicial_s','hr_electricidad_final_s')

class simbaAdmin(admin.ModelAdmin):
    search_fields = ['id_detalle_actividad', 'percusion', 'longitud']
    list_display = ('id_detalle_actividad', 'percusion', 'longitud')

class scoopAdmin(admin.ModelAdmin):
    search_fields = ['id_detalle_actividad', 'horometro', 'numero_cucharas','material','toneladas']
    list_display = ('id_detalle_actividad', 'horometro', 'numero_cucharas','material','toneladas')

##Modelos
class registroestadoAdmin(admin.ModelAdmin):
    search_fields = ['descripcion_registroestado']
    list_display = ('descripcion_registroestado',)

class entradaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion_entrada']
    list_display = ('descripcion_entrada',)

class platodefondoAdmin(admin.ModelAdmin):
    search_fields = ['descripcion_platodefondo']
    list_display = ('descripcion_platodefondo',)

class refrescoAdmin(admin.ModelAdmin):
    search_fields = ['descripcion_refresco']
    list_display = ('descripcion_refresco',)

class menuAdmin(admin.ModelAdmin):
    search_fields = ['id_entrada_1', 'id_entrada_2', 'id_platodefondo_1', 'id_platodefondo_2','id_refresco','id_operador','descripcion_menu','fecha_menu']
    list_display = ('id_entrada_1', 'id_entrada_2', 'id_platodefondo_1', 'id_platodefondo_2','id_refresco','id_operador','descripcion_menu','fecha_menu')

class pedidoAdmin(admin.ModelAdmin):
    search_fields = ['id_menu', 'id_operador', 'id_registroestado', 'fecha_pedido','descripcion_pedido']
    list_display = ('id_menu', 'id_operador', 'id_registroestado', 'fecha_pedido','descripcion_pedido')

class pedidoatendidoAdmin(admin.ModelAdmin):
    search_fields = ['id_pedido', 'id_operador', 'id_registroestado', 'fecha_atendido']
    list_display = ('id_pedido', 'id_operador', 'id_registroestado', 'fecha_atendido')


admin.site.register(models.operador,operadorAdmin)
admin.site.register(models.turno,turnoAdmin)
admin.site.register(models.equipo,equipoAdmin)
admin.site.register(models.actividad,actividadAdmin)
admin.site.register(models.detalle_actividad,detalle_actividadAdmin)
admin.site.register(models.simba,simbaAdmin)
admin.site.register(models.scoop,scoopAdmin)
##Modelos registrados
admin.site.register(models.registroestado,registroestadoAdmin)
admin.site.register(models.entrada,entradaAdmin)
admin.site.register(models.platodefondo,platodefondoAdmin)
admin.site.register(models.refresco,refrescoAdmin)
admin.site.register(models.menu,menuAdmin)
admin.site.register(models.pedido,pedidoAdmin)
admin.site.register(models.pedidoatendido,pedidoatendidoAdmin)
