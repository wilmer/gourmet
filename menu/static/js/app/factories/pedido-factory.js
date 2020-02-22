(function (module) {
    PedidoFactory.$inject = [
        'BaseFactory'
    ];
    function PedidoFactory(BaseFactory) {
        var actividad = [];
        var url = '/api/Pedido/';
        actividad.ObtenerPedido = function () {
            return BaseFactory.Obtener(url);
        };
        actividad.GuardarPedido = function (modelo) {
            return BaseFactory.Guardar(url, modelo);
        };
        actividad.EliminarPedido = function (modelo) {
            return BaseFactory.Eliminar(url, modelo);
        };
        return actividad;
    }
    module.factory('PedidoFactory', PedidoFactory);
})(angular.module("app-buenaventura"));
