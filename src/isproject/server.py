""" Server components """

from flask import Flask, request, make_response, render_template, send_from_directory
from flask.ext.restful import Api, Resource
from mongokit import Connection
from models import Node, Permission, Report, Session, Sim, User

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


class MongoResource(Resource):
    """ REST Resource for MongoDB using Mongokit """

    resource_name = None

    def get(self, _id):
        doc = conn[self.resource_name].one({"_id": _id})
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

    resource_name = "User"


api.add_resource(NodeResource, '/node/<_id>')
api.add_resource(PermissionResource, '/permission/<_id>')
api.add_resource(ReportResource, '/report/<_id>')
api.add_resource(SessionResource, '/session/<_id>')
api.add_resource(SimResource, '/sim/<_id>')
api.add_resource(UserResource, '/user/<_id>')


# Serves static resources like css, js, images, etc.
@app.route('/assets/<path:resource>')
def serveStaticResource(resource):
    # Return the static file
    return send_from_directory('static/assets/', resource)


@app.route('/')
def index_route():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
