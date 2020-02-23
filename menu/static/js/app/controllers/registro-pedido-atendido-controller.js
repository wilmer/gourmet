(function (module) {
/*
    RegistroDiarioController.$inject = ["$scope", "toastr", "PedidoFactory", "EquipoFactory",
     "TurnoFactory", "OperadorFactory", "DetalleActividadFactory"];
*/
RegistroPedidoAtendidoController.$inject = ["$scope", "toastr", "PedidoAtendidoFactory","PedidoFactory", "OperadorFactory","RegistroEstadoFactory"];
/*
    function RegistroDiarioController($scope, toastr, ActividadFactory, EquipoFactory, TurnoFactory,MenuFactory,
       OperadorFactory, DetalleActividadFactory,RegistroEstadoFactory) {
*/
         function RegistroPedidoAtendidoController($scope, toastr,PedidoAtendidoFactory,PedidoFactory,
            OperadorFactory,RegistroEstadoFactory) {

        //$scope.ListaActividad = [];
        $scope.ListaPedidoAtendido = [];
        $scope.ListaPedidoAtendidoHistorica = [];
        //$scope.ListaEquipo = [];
        //$scope.ListaTurno = [];
        $scope.ListaPedidoPendiente = [];
      //  $scope.ListaAyudante = [];
        $scope.ListaRegistroEstadoAtendida = [];

        $scope.ResetPedidoAtendido = function () {
            $scope.PedidoAtendido = {
                Id: 0,
                Estado: EstadoObjeto.SinCambios
            };
        }
        $scope.Iniciar = function () {
            //$scope.ResetActividad();
            //$scope.ObtenerEquipo();
            //$scope.ObtenerTurno();
            //$scope.ObtenerMenu();
            $scope.ObtenerPedidoPendiente();
            $scope.ObtenerRegistroEstadoPedido();
            //$scope.ObtenerActividad();
            //$scope.ObtenerAyudante();
        };
        $scope.ObtenerRegistroEstadoPedido = function () {
            RegistroEstadoFactory.ObtenerRegistroEstado().then(function (response) {
                $scope.ListaRegistroEstadoAtendida = response;
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
        $scope.CrearPedidoAtendido = function () {
            //$scope.ResetActividad();
            //$scope.Pedido.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-actividad');
        };
        $scope.CancelarPedidoAtendido = function () {
            Bootstrap.CerrarModal('#app-modal-actividad');
        };

        $scope.GuardarPedidoAtendido = function () {
            $scope.PedidoAtendido.id_operador = session_id_operador;
            $scope.PedidoAtendido.fecha_atendido = $scope.format($scope.PedidoAtendido.fecha);
            PedidoAtendidoFactory.GuardarPedidoAtendido($scope.Pedido).then(function (response) {
                toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                $scope.ObtenerPedidoAtentido();
            });
            Bootstrap.CerrarModal('#app-modal-actividad');
        };
        $scope.ObtenerPedidoAtentido = function () {
            $scope.ListaPedidoAtendido = [];
            $scope.ListaPedidoAtendidoHistorica = [];
            PedidoAtendidoFactory.ObtenerPedidoAtentido().then(function (response) {
                angular.forEach(response, function (item) {
                    if (item.id_operador == session_id_operador) {
                        //item.DetallesActividad = $scope.ObtenerDetalleActividad(item.id);
                        console.log(item);
                        if (item.fecha_atendido == '2020-02-22') {
                            $scope.ListaPedidoAtendido.push(item);
                        } else {
                            $scope.ListaPedidoAtendidoHistorica.push(item);
                        }
                    }
                });
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
        $scope.ObtenerRegistroEstadoPedido = function () {
            RegistroEstadoFactory.ObtenerRegistroEstado().then(function (response) {
                $scope.ListaRegistroEstado = response;
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
        $scope.ObtenerPedidoPendiente = function () {
            PedidoFactory.ObtenerPedido().then(function (response) {
                $scope.ListaPedidoPendiente = response;
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };


        $scope.format = function (date) {
            var d = new Date(date),
                month = '' + (d.getMonth() + 1),
                day = '' + d.getDate(),
                year = d.getFullYear();

            if (month.length < 2) month = '0' + month;
            if (day.length < 2) day = '0' + day;

            return [year, month, day].join('-');
        }
    }

    module.controller('RegistroPedidoAtendidoController', RegistroPedidoAtendidoController);

})(angular.module('app-buenaventura'));
