(function (module) {
    RegistroEstadoFactory.$inject = [
        'BaseFactory'
    ];
    function RegistroEstadoFactory(BaseFactory) {
        var turno = [];
        var url = '/api/RegistroEstado/';
        turno.ObtenerRegistroEstado = function () {
            return BaseFactory.Obtener(url);
        };
        turno.GuardarRegistroEstado = function (modelo) {
            return BaseFactory.Guardar(url, modelo);
        };
        turno.EliminarRegistroEstado = function (modelo) {
            return BaseFactory.Eliminar(url, modelo);
        };
        return turno;
    }
    module.factory('RegistroEstadoFactory', RegistroEstadoFactory);
})(angular.module("app-buenaventura"));
