function ReportController($scope, $resource) {

    var resourceUrl = '/report/'
    var resourceListUrl = '/reports'

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
            name: $scope.report.name,
            sim_id: $scope.report.sim_id,
            report_type: $scope.report.report_type,
            report_string: $scope.report.report_string,
            filename: $scope.report.filename
        });
        resource.$save();
        updateResourceList();
    };

    // Update the resources outright
    updateResourceList();
}
