from django.views.generic import View
from django.shortcuts import render, redirect
from menu.services.login_service import LoginService
from menu.dtos.usuario_dto import UsuarioDto


class LoginController(View):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.session.get('usuario', False):
            del request.session["usuario"]
        message = request.GET.get('message', None)
        return render(request, self.template_name, {'message': message})

    def post(self, request, *args, **kwargs):
        try:
            login_service = LoginService()
            usuario = request.POST.get('usuario', None)
            password = request.POST.get('password', None)
            usuario_dto = login_service.validar(usuario, password)
            request.session["id"] = usuario_dto.Id
            request.session["usuario"] = usuario_dto.Usuario
            request.session["nombre"] = usuario_dto.Nombre
            return redirect('/')
        except Exception as e:
            return render(request, self.template_name, {'message': e})
