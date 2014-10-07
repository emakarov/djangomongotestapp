from django.core.management.base import BaseCommand, CommandError
from timeseriesdata.models import Log
import random

class Command(BaseCommand):
    help = 'Fill the mongo databes with 1000 sample data'

    def handle(self, *args, **options):
        for i in xrange(0,1000):
            log = Log()
            log.data = random.random()*10000
            x = random.uniform(-90, 90)
            y = random.uniform(-180, 180)
            log.location = [x,y]
            log.save()
