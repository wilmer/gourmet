(function (module) {
    MenuFactory.$inject = [
        'BaseFactory'
    ];
    function MenuFactory(BaseFactory) {
        var menu = [];
        var url = '/api/Menu/';
        menu.ObtenerMenu = function () {
            return BaseFactory.Obtener(url);
        };
        menu.GuardarMenu = function (modelo) {
            return BaseFactory.Guardar(url, modelo);
        };
        menu.EliminarMenu = function (modelo) {
            return BaseFactory.Eliminar(url, modelo);
        };
        menu.ActualizarMenu = function (modelo) {
            return BaseFactory.Guardar(url, modelo);
        };
        return menu;
    }
    module.factory('MenuFactory', MenuFactory);
})(angular.module("app-buenaventura"));
