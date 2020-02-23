from rest_framework import serializers
from  menu import models

class Operadorserializer(serializers.HyperlinkedModelSerializer):
    # sexo_sexo = serializers.ChoiceField(choices=SEXO, default='1')
    class Meta:
        model = models.operador
        fields = ('id','nombre_operador', 'usuario', 'password', 'tipo_operador')



class Turnoserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.turno
        fields= ('id','descripcion_turno')

class Menuserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.menu
        fields= ('id','descripcion_menu')

class RegistroEstadoserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.registroestado
        fields= ('id','descripcion_registroestado')


class Equiposerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.equipo
        fields = ('id','nombre_equipo', 'modelo', 'estado')

class Actividadserializer(serializers.HyperlinkedModelSerializer):
    id_turno= serializers.PrimaryKeyRelatedField(many=False, queryset=models.turno.objects.all())
    id_operador = serializers.PrimaryKeyRelatedField(many=False, queryset=models.operador.objects.all())
    id_ayudante = serializers.PrimaryKeyRelatedField(many=False, queryset=models.operador.objects.all())
    id_equipo = serializers.PrimaryKeyRelatedField(many=False, queryset=models.equipo.objects.all())
    class Meta:
        model = models.actividad
        fields = ('id','id_turno', 'id_operador', 'id_ayudante', 'id_equipo', 'fecha_actividad', 'nivel')

class Pedidoserializer(serializers.HyperlinkedModelSerializer):
    id_menu= serializers.PrimaryKeyRelatedField(many=False, queryset=models.menu.objects.all())
    id_operador = serializers.PrimaryKeyRelatedField(many=False, queryset=models.operador.objects.all())
    id_registroestado = serializers.PrimaryKeyRelatedField(many=False, queryset=models.registroestado.objects.all())

    class Meta:
        model = models.pedido
        fields = ('id','id_menu', 'id_operador', 'id_registroestado','fecha_pedido')

class PedidoAtendidoserializer(serializers.HyperlinkedModelSerializer):
    id_pedido= serializers.PrimaryKeyRelatedField(many=False, queryset=models.pedido.objects.all())
    id_operador = serializers.PrimaryKeyRelatedField(many=False, queryset=models.operador.objects.all())
    id_registroestado = serializers.PrimaryKeyRelatedField(many=False, queryset=models.registroestado.objects.all())

    class Meta:
        model = models.pedidoatendido
        fields = ('id','id_pedido', 'id_operador', 'id_registroestado','fecha_atendido')


class Detalle_actividadserializer(serializers.HyperlinkedModelSerializer):
    id_actividad = serializers.PrimaryKeyRelatedField(many=False, queryset=models.actividad.objects.all())

    class Meta:
        model = models.detalle_actividad
        fields = ('id','id_actividad', 'actividad', 'hora_inicio', 'hora_fin','codigo_operacion','descripcion_operacion','labor_origen','labor_destino','observaciones','tipo_material','labor_s','proyecto_s','fila_s','num_taladro_s','num_barras_s','longitud_s','inclinacion_s','num_broca_s','hr_diesel_inicial','hr_diesel_final','hr_electricidad_inicial_s','hr_electricidad_final_s')


class Simbaserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.simba
        fields = ('id','id_detalle_actividad', 'percusion', 'longitud')



class Scoopserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.scoop
        fields = ('id','id_detalle_actividad', 'horometro', 'numero_cucharas', 'material', 'toneladas')
