from rest_framework import routers
from django.conf.urls import url,include
from menu.api import resources


router = routers.DefaultRouter()
router.register(r'Operador',resources.OperadorViewset,'OperadorList')
router.register(r'Turno',resources.TurnoViewset,'TurnoList')
router.register(r'Equipo',resources.EquipoViewset,'EquipoList')
router.register(r'Pedido',resources.PedidoViewset,'PedidoList')
router.register(r'Detalle_actividad',resources.Detalle_actividadViewset,'Detalle_actividadList')
router.register(r'Scoop',resources.SimbaViewset,'ScooplList')
router.register(r'Simba',resources.SimbaViewset,'SimbalList')
router.register(r'Menu',resources.MenuViewset,'MenuList')
router.register(r'RegistroEstado',resources.RegistroEstadoViewset,'RegistroEstadoList')



urlpatterns = [
    url(r'^', include(router.urls)),
]
