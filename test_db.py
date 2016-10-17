from mongoengine import *
from mlab import *

class Pet(Document):
    name = StringField()
    nickname = StringField()
    description = StringField()

class Owner(Document):
    name = StringField()
    pet = EmbeddedDocumentField("Pet")

mlab_connect()

o = Owner(name = "Manh")
o.pet = Pet(name="Lulu")

o.save()