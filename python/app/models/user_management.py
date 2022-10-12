from mongoengine import *
from datetime import datetime
from app import configs

connect(alias='db_user_management', db = configs.db_name)
class Roles(Document):
    roleName = StringField(required=True, unique=True)
    meta = {'db_alias': 'db_user_management'}

class Users(Document):
    roleId = ReferenceField(Roles)
    userName = StringField(max_length=25, required=True, unique=True)
    userEmail = EmailField(required=True, unique=True)
    userPassword = StringField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())

    meta = {'db_alias': 'db_user_management'}