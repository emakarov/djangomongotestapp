from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api

api_v1 = Api(api_name='v1')

from timeseriesdata import api
api_v1.register(api.LogResource())

urlpatterns = patterns('',
    (r'', include(api_v1.urls)),
)
