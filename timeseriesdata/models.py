from django.db import models
from mongoengine import Document, fields
import datetime

# Create your models here.

class Log(Document):
    data = fields.FloatField(required=True)
    ts = fields.DateTimeField(default=datetime.datetime.now)
    location = fields.GeoPointField(required=False)

    


