from mongoengine import *
from faker import Faker
import mlab
mlab.connect()

class Gift(Document):
    gift = StringField()
    gift_name = StringField()

#gift = Gift(gift = "https://docs.google.com/uc?id=0ByQk_BXnNoNfQjNBRDRkWGc1a1k", gift_name = "BUY 1 GET 1 MAC ")
#gift.save()
