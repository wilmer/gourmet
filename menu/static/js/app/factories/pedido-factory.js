(function (module) {
    PedidoFactory.$inject = [
        'BaseFactory'
    ];
    function PedidoFactory(BaseFactory) {
        var pedido = [];
        var url = '/api/Pedido/';
        pedido.ObtenerPedido = function () {
            return BaseFactory.Obtener(url);
        };
        pedido.GuardarPedido = function (modelo) {
            return BaseFactory.Guardar(url, modelo);
        };
        pedido.EliminarPedido = function (modelo) {
            return BaseFactory.Eliminar(url, modelo);
        };
        return pedido;
    }
    module.factory('PedidoFactory', PedidoFactory);
})(angular.module("app-buenaventura"));
