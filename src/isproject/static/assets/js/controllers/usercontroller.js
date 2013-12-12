/*
 * This defines the controller that handles loading and
 * saving of users via the REST interface.
 *
 */
function UserController($scope, $resource) {
    // Define a new user resource that will simplify interaction between
    //  the web server and the client
    var User = $resource('/user/:username', { username: '@username' },
                         { save: { method: 'PUT', url: '/user/:username' } }
    );
    // This is for getting all the users, technically, it is a
    // different resource than 'User'
    var Users = $resource('/users');

    // Loads all the users from the server and updates the scopes
    // copy of users
    function updateUsers() {
        Users.query({}, function(result) {
            $scope.users = result;
        });
     }

     // Deletes a user and updates the display
    $scope.deleteUser = function(username) {
        User.remove({ username: username });
        updateUsers();
    }

    // Creates a new User resource and saves a new record
    // if it doesn't exist, and updates it if it does
    $scope.addUpdateUser = function() {
        var user = new User({
            username: $scope.username,
            firstName: $scope.firstName,
            lastName: $scope.lastName
        });
        user.$save();
        updateUsers();
    };

    // Here, I'm adding an extra method to my user resource that
    // will let me get their full name is a simple fashion
    angular.extend(Users.prototype, {
        getFullName: function() {
            return this.lastName + ', ' + this.firstName;
        }
    });

    // Update the users outright
    updateUsers();
}
