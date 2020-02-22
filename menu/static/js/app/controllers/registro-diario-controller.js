(function (module) {
/*
    RegistroDiarioController.$inject = ["$scope", "toastr", "PedidoFactory", "EquipoFactory",
     "TurnoFactory", "OperadorFactory", "DetalleActividadFactory"];
*/
RegistroDiarioController.$inject = ["$scope", "toastr", "PedidoFactory","MenuFactory", "OperadorFactory","RegistroEstadoFactory"];
/*
    function RegistroDiarioController($scope, toastr, ActividadFactory, EquipoFactory, TurnoFactory,MenuFactory,
       OperadorFactory, DetalleActividadFactory,RegistroEstadoFactory) {
*/
         function RegistroDiarioController($scope, toastr,PedidoFactory,MenuFactory,
            OperadorFactory,RegistroEstadoFactory) {

        //$scope.ListaActividad = [];
        $scope.ListaPedido = [];
        $scope.ListaPedidoHistorica = [];
        //$scope.ListaEquipo = [];
        //$scope.ListaTurno = [];
        $scope.ListaMenu = [];
      //  $scope.ListaAyudante = [];
        $scope.ListaRegistroEstado = [];

        $scope.ResetPedido = function () {
            $scope.Pedido = {
                Id: 0,
                Estado: EstadoObjeto.SinCambios
            };
        }
        $scope.Iniciar = function () {
            //$scope.ResetActividad();
            //$scope.ObtenerEquipo();
            //$scope.ObtenerTurno();
            $scope.ObtenerMenu();
            $scope.ObtenerPedido();
            $scope.ObtenerRegistroEstado();
            //$scope.ObtenerActividad();
            //$scope.ObtenerAyudante();
        };
        $scope.CrearPedido = function () {
            //$scope.ResetActividad();
            //$scope.Pedido.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-actividad');
        };
        $scope.CancelarPedido = function () {
            Bootstrap.CerrarModal('#app-modal-actividad');
        };

        $scope.GuardarPedido = function () {
            $scope.Pedido.id_operador = session_id_operador;
            $scope.Pedido.fecha_pedido = $scope.format($scope.Pedido.fecha);
            PedidoFactory.GuardarPedido($scope.Pedido).then(function (response) {
                toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                $scope.ObtenerPedido();
            });
            Bootstrap.CerrarModal('#app-modal-actividad');
        };
        $scope.ObtenerPedido = function () {
            $scope.ListaPedido = [];
            $scope.ListaPedidoHistorica = [];
            PedidoFactory.ObtenerPedido().then(function (response) {
                angular.forEach(response, function (item) {
                    if (item.id_operador == session_id_operador) {
                        //item.DetallesActividad = $scope.ObtenerDetalleActividad(item.id);
                        console.log(item);
                        if (item.fecha_pedido == '2020-02-22') {
                            $scope.ListaPedido.push(item);
                        } else {
                            $scope.ListaPedidoHistorica.push(item);
                        }
                    }
                });
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
        $scope.ObtenerMenu = function () {
            MenuFactory.ObtenerMenu().then(function (response) {
                $scope.ListaMenu = response;
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
        $scope.ObtenerRegistroEstado = function () {
            RegistroEstadoFactory.ObtenerRegistroEstado().then(function (response) {
                $scope.ListaRegistroEstado = response;
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

    module.controller('RegistroDiarioController', RegistroDiarioController);

})(angular.module('app-buenaventura'));
