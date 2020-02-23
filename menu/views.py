from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import decorator_from_middleware

from menu.middlewares.autenticacion_middleware import AutenticacionMiddleware


@decorator_from_middleware(AutenticacionMiddleware)
def dashboard(request):
    return render(request, 'dashboard.html', get_user(request))


@decorator_from_middleware(AutenticacionMiddleware)
def registro_diario(request):
    return render(request, 'registro_diario.html', get_user(request))

@decorator_from_middleware(AutenticacionMiddleware)
def registro_atencion_pedidos(request):
    return render(request, 'registro_atencion_pedidos.html', get_user(request))


@decorator_from_middleware(AutenticacionMiddleware)
def gestion_inicio(request):
    return render(request, 'gestion/inicio.html', get_user(request))


@decorator_from_middleware(AutenticacionMiddleware)
def gestion_operador(request):
    return render(request, 'gestion/operador.html', get_user(request))


def get_user(request):
    return {
        'id' : request.session.get('id', False),
        'nombre' : request.session.get('nombre', False)
    }
