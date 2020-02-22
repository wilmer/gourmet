(function (module) {

    BaseFactory.$inject = [
        '$resource'
    ];

    function BaseFactory($resource) {

        var servicio = [];

        servicio.Obtener = function (ruta, modelo) {
            return $resource(ruta, modelo, {
                Get: {
                    method: 'GET',
                    isArray: true,
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json"
                    }
                }
            }).Get().$promise;
        };

        servicio.Guardar = function (ruta, modelo) {
            return $resource(ruta, {}, {
                Post: {
                    method: 'POST',
                    isArray: false,
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json"
                    }
                }
            }).Post(modelo).$promise;
        };

        servicio.Eliminar = function (ruta, modelo) {
            return $resource(ruta + modelo.id + '/', {}, {
                Delete: {
                    method: 'DELETE',
                    isArray: false,
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json"
                    }
                }
            }).Delete().$promise;
        };

        return servicio;
    }

    module.factory('BaseFactory', BaseFactory);

})(angular.module("app-buenaventura"));