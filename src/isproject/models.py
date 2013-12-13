from mongokit import Document, OR
from datetime import datetime
from bson.objectid import ObjectId

class Node(Document):

    __database__ = "ncs"
    __collection__ = "nodes"

    """
    structure = {
        "label": unicode,
        "ip_address": unicode,
        "status": unicode,
        "resources": [
            {
                "type": unicode,
                "properties": OR(
                    {
                        "make": unicode,
                        "series": unicode,
                        "cores": int
                    },
                    {
                        "name": unicode,
                        "compute_capability": float,
                        "cores": int
                    }
                )
            }
        ]
    }
    """

    structure = {
        "label": unicode,
        "ip_address": unicode,
        "status": unicode,
        "resources": [
            {
                "type": unicode,
                "properties": {
                    "make": unicode,
                    "series": unicode,
                    "cores": int
                }
            }
        ]
    }

class Permission(Document):

    __database__ = "ncs"
    __collection__ = "permissions"

    structure = {
        "name": unicode
    }

class Report(Document):

    __database__ = "ncs"
    __collection__ = "report"

    structure = {
        "name": unicode,
        "sim_id": unicode,
        "report_type": unicode,
        "report_string": unicode,
        "filename": unicode
    }

class Session(Document):

    __database__ = "ncs"
    __collection__ = "sessions"

    structure = {
        "user": unicode,
        "created": datetime
    }

class Sim(Document):

    __database__ = "ncs"
    __collection__ = "sims"

    structure = {
        "session": unicode,
        "start_time": datetime,
        "end_time": datetime,
        "reports": [ObjectId]
    }

class User(Document):

    __database__ = "ncs"
    __collection__ = "users"

    structure = {
        "username": unicode,
        "first_name": unicode,
        "last_name": unicode,
        "email": unicode,
        "permissions": [ObjectId]
    }
