""" Server components """

from flask import Flask, request, make_response, render_template, send_from_directory
from flask.ext.restful import Api, Resource
from mongokit import Connection
from models import Node, Permission, Report, Session, Sim, User
import json
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

conn = Connection(host="localhost", port=27017)

conn.register([
    Node,
    Permission,
    Report,
    Session,
    Sim,
    User
])

pages = [
    ("Home", "/"),
    ("Users", "/pages/users"),
    ("Nodes", "/pages/nodes"),
    ("Reports", "/pages/reports"),
    ("Sessions", "/pages/sessions"),
    ("Sims", "/pages/sims"),
    ("Permissions", "/pages/permissions")
]


def resolve_object(_id, collection):
    print conn[collection].one({"_id": _id})
    return conn[collection].one({"_id": _id})


class MongoResource(Resource):
    """ REST Resource for MongoDB using Mongokit """

    resource_name = None

    def get(self, _id):
        doc = conn[self.resource_name].one({"_id": unicode(_id)})
        if not doc:
            return make_response(("", 204, []))
        else:
            return doc.to_json()

    def put(self, _id):
        data = request.get_data()
        try:
            doc = conn[self.resource_name].from_json(data)
        except KeyError:
            return make_response(("", 400, []))
        doc.save()
        return

    def delete(self, _id):
        doc = conn[self.resource_name].one({"_id": _id})
        if not doc:
            return make_response(("", 204, []))
        doc.delete()
        return


class NodeResource(MongoResource):

    resource_name = "Node"


class PermissionResource(MongoResource):

    resource_name = "Permission"


class ReportResource(MongoResource):

    resource_name = "Report"


class SessionResource(MongoResource):

    resource_name = "Session"


class SimResource(MongoResource):

    resource_name = "Sim"


class UserResource(MongoResource):

    def get(self, _id):
        doc = super(MongoResource, self).get(_id)
        permission_objects = []
        for permission in doc.permissions:
            obj = conn["Permission"].one({"_id": permission})
            permission_objects.append(obj)
        doc.permissions = permission_objects
        return doc

    resource_name = "User"


class PluralResource(Resource):

    resource_name = None

    def get(self):
        resources = list(conn[self.resource_name].find())
        return make_response(json.dumps(resources))


class NodesResource(PluralResource):

    resource_name = "Node"


class UsersResource(PluralResource):

    resource_name = "User"

    def get(self):
        resources = list(conn[self.resource_name].find())
        res = ""
        for user in resources:
            permissions = []
            for permission in user['permissions']:
                permissions.append(resolve_object(permission, "Permission"))
            user['permissions'] = permissions
            res = res + user.to_json() + ","
        res = "[" + res[0:len(res) - 1] + "]"
        return make_response(res)


class PermissionsResource(PluralResource):

    resource_name = "Permission"


class ReportsResource(PluralResource):

    resource_name = "Report"


class SessionsResource(PluralResource):

    resource_name = "Session"


class SimsResource(PluralResource):

    resource_name = "Sim"


# Add singular resources
api.add_resource(NodeResource, '/node/<_id>')
api.add_resource(PermissionResource, '/permission/<_id>')
api.add_resource(ReportResource, '/report/<_id>')
api.add_resource(SessionResource, '/session/<_id>')
api.add_resource(SimResource, '/sim/<_id>')
api.add_resource(UserResource, '/user/<_id>')

# Add plural resources
api.add_resource(NodesResource, '/nodes')
api.add_resource(UsersResource, '/users')
api.add_resource(PermissionsResource, '/permissions')
api.add_resource(ReportsResource, '/reports')
api.add_resource(SessionsResource, '/sessions')
api.add_resource(SimsResource, '/sims')


# Serves static resources like css, js, images, etc.
@app.route('/assets/<path:resource>')
def serveStaticResource(resource):
    # Return the static file
    return send_from_directory('static/assets/', resource)


@app.route('/')
def index_route():
    return render_template('index.html', title="Home", pages=pages)


@app.route('/pages/nodes')
def node_page_route():
    return render_template('nodes.html', title="Nodes", pages=pages)


@app.route('/pages/users')
def user_page_route():
    return render_template('users.html', title="Users", pages=pages)


@app.route('/pages/permissions')
def permission_page_route():
    return render_template('permissions.html', title="Permissions", pages=pages)


@app.route('/pages/reports')
def report_page_route():
    return render_template('reports.html', title="Reports", pages=pages)


@app.route('/pages/sessions')
def session_page_route():
    return render_template('sessions.html', title="Sessions", pages=pages)


@app.route('/pages/sims')
def sims_page_route():
    return render_template('sims.html', title="Sims", pages=pages)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
