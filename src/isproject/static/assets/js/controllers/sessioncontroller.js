function SessionController($scope, $resource) {

    var resourceUrl = '/session/'
    var resourceListUrl = '/sessions'

    var Resource = $resource(resourceUrl + ':_id',
                         { _id: '@_id' },
                         { save: { method: 'PUT', url: resourceUrl + ':_id' } }
    );

    var ResourceList = $resource(resourceListUrl);

    function updateResourceList() {
        ResourceList.query({}, function(result) {
            $scope.resourceList = result;
        });
    }

    $scope.deleteResource = function(_id) {
        Resource.remove({ _id: _id });
        updateResourceList();
    }

    $scope.addResource = function() {
        var resource_id = String(Math.round(Math.random() * Math.pow(2, 64)))
        var resource = new Resource({
            _id: resource_id,
            user: $scope.session.user,
            created: $scope.session.created
        });
        resource.$save();
        updateResourceList();
    };

    // Update the resources outright
    updateResourceList();
}
