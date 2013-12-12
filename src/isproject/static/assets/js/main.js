/*
 * Create a new Angular module for our application.
 * ngResource is another angular module we are requiring as
 * a dependency here to handle the REST stuff that is normally
 * done manually.
 *
 */
var AppModule = angular.module('isproject', ['ngResource']);

/*
 * Register the NodeController with the module
 *
 */
AppModule = AppModule.controller('NodeController', NodeController);
