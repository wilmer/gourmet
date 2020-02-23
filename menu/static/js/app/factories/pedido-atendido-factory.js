(function (module) {
    PedidoAtendidoFactory.$inject = [
        'BaseFactory'
    ];
    function PedidoAtendidoFactory(BaseFactory) {
        var pedidoatendido = [];
        var url = '/api/PedidoAtendido/';
        pedidoatendido.ObtenerPedidoAtentido = function () {
            return BaseFactory.Obtener(url);
        };
        pedidoatendido.GuardarPedidoAtendido = function (modelo) {
            return BaseFactory.Guardar(url, modelo);
        };
        pedidoatendido.EliminarPedidoAtendido = function (modelo) {
            return BaseFactory.Eliminar(url, modelo);
        };
        return pedidoatendido;
    }
    module.factory('PedidoAtendidoFactory', PedidoAtendidoFactory);
})(angular.module("app-buenaventura"));
