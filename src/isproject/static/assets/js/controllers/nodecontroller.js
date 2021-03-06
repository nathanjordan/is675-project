function NodeController($scope, $resource) {

    var resourceUrl = '/node/'
    var resourceListUrl = '/nodes'

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
            label: $scope.node.label,
            ip_address: $scope.node.ip_address,
            status: "online",
            resources: [],
        });
        resource.$save();
        updateResourceList();
    };

    // Update the resources outright
    updateResourceList();
}
