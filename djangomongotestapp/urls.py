from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangomongotestapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'timeseriesdata.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^api/',include('apiurls')),
)
