(function (module) {
    MenuFactory.$inject = [
        'BaseFactory'
    ];
    function MenuFactory(BaseFactory) {
        var turno = [];
        var url = '/api/Menu/';
        turno.ObtenerMenu = function () {
            return BaseFactory.Obtener(url);
        };
        turno.GuardarMenu = function (modelo) {
            return BaseFactory.Guardar(url, modelo);
        };
        turno.EliminarMenu = function (modelo) {
            return BaseFactory.Eliminar(url, modelo);
        };
        return turno;
    }
    module.factory('MenuFactory', MenuFactory);
})(angular.module("app-buenaventura"));
