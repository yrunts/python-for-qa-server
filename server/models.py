
import json


clients_data = '''
[
   {"name": "admin", "password": "password"},
   {"name": "user1", "password": "user1"},
   {"name": "user2", "password": "user2"},
   {"name": "user3", "password": "user3"},
   {"name": "user4", "password": "user4"},
   {"name": "user5", "password": "user5"},
   {"name": "user6", "password": "user6"},
   {"name": "user7", "password": "user7"},
   {"name": "user8", "password": "user8"},
   {"name": "user9", "password": "user9"},
   {"name": "user10", "password": "user10"},
   {"name": "user11", "password": "user11"},
   {"name": "user12", "password": "user12"},
   {"name": "user13", "password": "eSG23JkCif"},
   {"name": "user14", "password": "user14"},
   {"name": "user15", "password": "user15"},
   {"name": "user16", "password": "user16"},
   {"name": "user17", "password": "user17"},
   {"name": "user18", "password": "r3j5Vd7Hiy"},
   {"name": "user19", "password": "user19"},
   {"name": "user20", "password": "user20"},
   {"name": "user21", "password": "user21"}
]
'''


users = []


class User(object):

    def __init__(self, name, password):
        self.name = name
        self.password = password


def get_user(name):
    for user in users:
        if user.name == name:
            return user
    return None


def init_users():
    global users
    clients = json.loads(clients_data)
    users.extend([User(c['name'], c['password']) for c in clients])
