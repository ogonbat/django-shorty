from django.conf.urls.defaults import patterns, url
from shorty.api.handlers import get_info

urlpatterns = patterns('',
   url(r'^short$', get_info),
   url(r'^short/(?P<slug>[\a-zA-Z0-9\-]+)/$', get_info),
)