from django.conf.urls.defaults import patterns, url
from shorty.api.handlers import ShortenHandler
from shorty.piston.authentication import HttpBasicAuthentication
from shorty.piston.resource import Resource

auth = HttpBasicAuthentication(realm="Shorty-Auth")
shorten_handler = Resource(ShortenHandler, authentication=auth)
urlpatterns = patterns('',
   url(r'^shorten$', shorten_handler, { 'emitter_format': 'json' }),
)