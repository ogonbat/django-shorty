from shorty.models import Url
from django.views.decorators.http import require_http_methods
from shorty.utils import url_decode
from django.core import serializers
from django.http import Http404

@require_http_methods(['GET'])
def get_info(self,request,slug=None):
    base = Url.objects
    if slug != None:
        try:
            values = base.filter(user=request.user,id=url_decode(slug))
            return serializers.serialize("json",values,fields={'url_field','personal_slug','status','slug','created'})
        except Url.DoesNotExist:
            return Http404
    else:
        try:
            values = base.filter(user=request.user)
            return serializers.serialize("json",values,fields={'url_field','personal_slug','status','slug','created'})
        except Url.DoesNotExist:
            return Http404