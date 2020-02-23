from django.urls import path, include
from . import views
from menu.controllers.login_controller import LoginController

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('registro_diario', views.registro_diario, name='registro_diario'),
    path('registro_atencion_pedidos', views.registro_atencion_pedidos, name='registro_atencion_pedidos'),
    #path('registro_pedido', views.registro_diario, name='registro_pedido'),

    path('login', LoginController.as_view(), name='login'),
    path('gestion', views.gestion_inicio, name='gestion_inicio'),
    path('gestion/operador', views.gestion_operador, name='gestion_operador'),
]
