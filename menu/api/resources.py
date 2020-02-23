from rest_framework import  viewsets
from menu import models
from . import serializers

class OperadorViewset(viewsets.ModelViewSet):
	queryset=models.operador.objects.all()
	serializer_class=serializers.Operadorserializer

class TurnoViewset(viewsets.ModelViewSet):
	queryset=models.turno.objects.all()
	serializer_class=serializers.Turnoserializer

class MenuViewset(viewsets.ModelViewSet):
	queryset=models.menu.objects.all()
	serializer_class=serializers.Menuserializer

class RegistroEstadoViewset(viewsets.ModelViewSet):
	queryset=models.registroestado.objects.all()
	serializer_class=serializers.RegistroEstadoserializer


class EquipoViewset(viewsets.ModelViewSet):
    queryset = models.equipo.objects.all()
    serializer_class = serializers.Equiposerializer


class ActividadViewset(viewsets.ModelViewSet):
    queryset = models.actividad.objects.all()
    serializer_class = serializers.Actividadserializer

class PedidoViewset(viewsets.ModelViewSet):
    queryset = models.pedido.objects.all()
    serializer_class = serializers.Pedidoserializer

class PedidoAtendidoViewset(viewsets.ModelViewSet):
    queryset = models.pedidoatendido.objects.all()
    serializer_class = serializers.PedidoAtendidoserializer


class Detalle_actividadViewset(viewsets.ModelViewSet):
    queryset = models.detalle_actividad.objects.all()
    serializer_class = serializers.Detalle_actividadserializer

class SimbaViewset(viewsets.ModelViewSet):
    queryset = models.simba.objects.all()
    serializer_class = serializers.Simbaserializer

class ScoopViewset(viewsets.ModelViewSet):
    queryset = models.scoop.objects.all()
    serializer_class = serializers.Scoopserializer
