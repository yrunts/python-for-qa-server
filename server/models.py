
import json


clients_data = '''
[
   {"name": "admin", "password": "password"}
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
