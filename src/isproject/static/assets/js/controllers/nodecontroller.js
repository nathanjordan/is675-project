/*
 * This defines the controller that handles loading and
 * saving of nodes via the REST interface.
 *
 */
function NodeController($scope, $resource) {

    var Node = $resource('/node/:_id', { _id: '@_id' },
                         { save: { method: 'PUT', url: '/node/:_id' } }
    );

    var Nodes = $resource('/nodes');

    function updateNodes() {
        Nodes.query({}, function(result) {
            $scope.nodes = result;
        });
    }

    $scope.deleteNode = function(_id) {
        Node.remove({ _id: _id});
        updateNodes();
    }

    $scope.addUpdateNode = function() {
        var node = new Node({
            username: $scope.username,
            firstName: $scope.firstName,
            lastName: $scope.lastName
        });
        node.$save();
        updateNodes();
    };

    updateNodes();
}
