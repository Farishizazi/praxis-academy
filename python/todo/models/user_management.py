from mongoengine import *
from todo import configs

connect(alias='db_user_management', db = configs.db_name)

class Tables(Document):
    title = StringField(required=True, unique=True)
    description = StringField(null=True, unique=True)
    
    meta = {'db_alias': 'db_user_management'}