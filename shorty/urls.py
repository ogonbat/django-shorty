from django.conf.urls.defaults import patterns, url, include
from shorty.views import shorty_url, add_shorty_url, get_auth_token

__author__ = 'cingusoft'

urlpatterns = patterns('shorty.views',
            url(r'^add/$',add_shorty_url,{},name="add_shorty_url"),
            url(r'^token/request/$',get_auth_token,{},name="get_token_request"),
            url(r'^(?P<slug>[\a-zA-Z0-9\-]+)/$',shorty_url,{},name="shorty_url"),
            (r'^api/', include('shorty.api.urls')),
)