#from django.db import models

# Create your models here.

from mongoengine import *
connect('mongodb://user:user@ac-zvbacnb-shard-00-02.n4s7ayo.mongodb.net:27017/?ssl=true&replicaSet=atlas-89iqf1-shard-0&authSource=admin&retryWrites=true&w=majority')
class User(Document):
   mail=EmailField()
   username = StringField()
   password=StringField(min_value=8, max-value=20)
