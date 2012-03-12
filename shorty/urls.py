'''
Created on 12/03/2012

@author: amucci
'''
from django.conf.urls.defaults import patterns, url
from shorty.views import shorty_url, add_shorty_url


__author__ = 'cingusoft'

urlpatterns = patterns('shorty.views',
            url(r'^/',add_shorty_url,{},name="add_shorty_url"),
            url(r'^(?P<slug>[\a-zA-Z0-9\-]+)/',shorty_url,{},name="shorty_url"),
)