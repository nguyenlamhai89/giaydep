from mongoengine import *

class User(Document):
    username = StringField()
    password = StringField()

# user = User()
# user.save()
