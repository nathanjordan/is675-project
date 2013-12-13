function SimController($scope, $resource) {

    var resourceUrl = '/sim/'
    var resourceListUrl = '/sims'

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
            session: $scope.sim.session,
            start_time: $scope.sim.start_time,
            end_time: $scope.sim.end_time,
            reports: [],
        });
        resource.$save();
        updateResourceList();
    };

    // Update the resources outright
    updateResourceList();
}
