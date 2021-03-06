function UserController($scope, $resource) {

    var resourceUrl = '/user/'
    var resourceListUrl = '/users'

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
            username: $scope.user.username,
            first_name: $scope.user.first_name,
            last_name: $scope.user.last_name,
            email: $scope.user.email,
            permissions: []
        });
        resource.$save();
        updateResourceList();
    };

    // Update the resources outright
    updateResourceList();
}
