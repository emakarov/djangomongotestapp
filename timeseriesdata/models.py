from django.db import models
from mongoengine import Document, fields
import datetime

# Create your models here.

class Log(Document):
    data = fields.StringField(max_length=200, required=True)
    ts = fields.DateTimeField(default=datetime.datetime.now)
    location = fields.GeoPointField(auto_index=False)

    


