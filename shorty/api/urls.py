from django.conf.urls.defaults import patterns, url
from shorty.api.handlers import ShortenHandler
from piston.authentication import HttpBasicAuthentication,\
    OAuthAuthentication
from piston.resource import Resource

auth = HttpBasicAuthentication(realm="Shorty-Auth")
oauth = OAuthAuthentication()
shorten_handler = Resource(ShortenHandler, authentication=oauth)
urlpatterns = patterns('',
   url(r'^short$', shorten_handler, { 'emitter_format': 'json' }),
   url(r'^short/(?P<slug>[\a-zA-Z0-9\-]+)/$', shorten_handler, { 'emitter_format': 'json' }),
)