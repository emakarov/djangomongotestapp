#from tastypie import authorization
from tastypie_mongoengine import resources
import models

class LogResource(resources.MongoEngineResource):
    class Meta:
        queryset = models.Log.objects.all()
        allowed_methods = ('get', 'post', 'put', 'delete')
        #authorization = authorization.Authorization()
        resource_name = 'timeseriesdata/log' 
