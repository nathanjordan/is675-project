from mongokit import Connection
from models import Node, Permission, Report, Session, Sim, User
from datetime import datetime

conn = Connection(host="localhost", port=27017)

TIME_FORMAT = "%m/%d/%Y %I:%M:%s %p %Z"

conn.register([
    Node,
    Permission,
    Report,
    Session,
    Sim,
    User
])

# Permissions

permission1 = conn.ncs.permissions.Permission()
permission2 = conn.ncs.permissions.Permission()

permission1['_id'] = unicode('998948321893847918374')
permission1['name'] = unicode('Run Simulations')

permission2['_id'] = unicode('677423984897987289799')
permission2['name'] = unicode('User Management')

permission1.save()
permission2.save()

# Users

user1 = conn.ncs.users.User()
user2 = conn.ncs.users.User()

user1['_id'] = unicode('19028301283092183102')
user1['username'] = unicode('njordan')
user1['first_name'] = unicode('Nathan')
user1['last_name'] = unicode('Jordan')
user1['email'] = unicode('njordan@cse.unr.edu')
user1['permissions'] = [unicode(permission1['_id'])]

user2['_id'] = unicode('4587364923894293923')
user2['username'] = unicode('dana')
user2['first_name'] = unicode('Dana')
user2['last_name'] = unicode('Edberg')
user2['email'] = unicode('edberg@unr.edu')
user2['permissions'] = []

user1.save()
user2.save()

# Sessions

session1 = conn.ncs.sessions.Session()
session2 = conn.ncs.sessions.Session()

session1['_id'] = unicode('7735827638946929874')
session1['user'] = unicode(user1['_id'])
session1['created'] = unicode(datetime.now().strftime(TIME_FORMAT))

session2['_id'] = unicode('8748362982936492634')
session2['user'] = unicode(user2['_id'])
session2['created'] = unicode(datetime.today().strftime(TIME_FORMAT))

session1.save()
session2.save()

# Reports

report1 = conn.ncs.reports.Report()
report2 = conn.ncs.reports.Report()

sim1_id = '0934820384932852039582'

report1['_id'] = unicode('72878327893248932729')
report1['name'] = unicode('Report1')
report1['sim_id'] = unicode(sim1_id)
report1['report_type'] = unicode('voltage')
report1['report_string'] = unicode('fdsa:fdasfga:fdsafdsa')
report1['filename'] = unicode('report1.txt')

report2['_id'] = unicode('7827387487398279923')
report2['name'] = unicode('Report2')
report2['sim_id'] = unicode(sim1_id)
report2['report_type'] = unicode('voltage')
report2['report_string'] = unicode('fkldjs:isjdfiousa:fdsa')
report2['filename'] = unicode('report2.txt')

report1.save()
report2.save()

# Sims

sim1 = conn.ncs.sims.Sim()
sim2 = conn.ncs.sims.Sim()

sim1['_id'] = unicode('0934820384932852039582')
sim1['session'] = unicode(session1['_id'])
sim1['start_time'] = unicode(datetime.today().strftime(TIME_FORMAT))
sim1['end_time'] = unicode(datetime.now().strftime(TIME_FORMAT))
sim1['reports'] = [unicode(report1['_id']), unicode(report2['_id'])]

sim2['_id'] = unicode('786732873748638726478327')
sim2['session'] = unicode(session2['_id'])
sim2['start_time'] = unicode(datetime.today().strftime(TIME_FORMAT))
sim2['end_time'] = unicode(datetime.now().strftime(TIME_FORMAT))
sim2['reports'] = []

sim1.save()
sim2.save()

node1 = conn.ncs.nodes.Node()
node2 = conn.ncs.nodes.Node()

node1['_id'] = unicode('8749274982374982347323')
node1['label'] = unicode('brain1')
node1['ip_address'] = unicode('10.0.0.1')
node1['status'] = unicode('online')
node1['resources'] = [
    {
        "type": unicode("CPU"),
        "properties": {
            "make": unicode("AMD"),
            "series": unicode("Phenom 2"),
            "cores": 6
        }
    },
    {
        "type": unicode("CUDA"),
        "properties": {
            "make": unicode("NVIDIA"),
            "series": unicode("GTX580"),
            "cores": 512
        }
    },
]

node2['_id'] = unicode('792834798378274292384')
node2['label'] = unicode('brain2')
node2['ip_address'] = unicode('10.0.0.2')
node2['status'] = unicode('online')
node2['resources'] = [
    {
        "type": unicode("CPU"),
        "properties": {
            "make": unicode("AMD"),
            "series": unicode("Phenom 2"),
            "cores": 6
        }
    }
]

node1.save()
node2.save()
