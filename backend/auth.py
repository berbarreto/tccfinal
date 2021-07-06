from firebase_admin.auth import verify_id_token

from database import User, Doctor

users = {
    "oi": User(id=1)
}

#
# class Dummy:
#     id = 0
#
#     def __init__(self, id):
#         self.id = id
#

doctors = {
    "oi": Doctor(id=1)
}


def login_user(token, user):
    print("LOGINNNNNNN")
    # verify_id_token()
    users[str(token)] = user


def login_doctor(token, doctor):
    doctors[str(token)] = doctor


def get_user(token):
    return users[token]


def get_doctor(token):
    return doctors[token]
