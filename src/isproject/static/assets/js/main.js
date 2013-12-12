AppModule = angular.module('isproject', ['ngRoute', 'ngResource']);

AppModule = AppModule.controller('UserController', UserController);
AppModule = AppModule.controller('NodeController', NodeController);
AppModule = AppModule.controller('PermissionController', PermissionController);

angular.bootstrap(document, ['isproject']);
