from shorty.models import Url
from django.views.decorators.http import require_http_methods
from shorty.utils import url_decode
from django.http import Http404, HttpResponse
from django.utils import simplejson
import time

@require_http_methods(['GET'])

def get_info(request,slug=None):
    base = Url.objects
    if slug != None:
        try:
            values = base.filter(user=request.user,id=url_decode(slug))
            json = simplejson.dumps( [{'slug': o.slug,
                                       'personal_slug': o.personal_slug,
                                       'url': o.url_field,
                                       'status': o.status,
                                       'created': time.strftime('%Y-%m-%d %H:%M:%SZ', o.created.utctimetuple())
                                       } for o in values] )
            return HttpResponse(json,mimetype="application/json")
        except Url.DoesNotExist:
            return Http404
    else:
        try:
            values = base.filter(user=request.user)
            json = simplejson.dumps( [{'slug': o.slug,
                                       'personal_slug': o.personal_slug,
                                       'url': o.url_field,
                                       'status': o.status,
                                       'created': time.strftime('%Y-%m-%d %H:%M:%SZ', o.created.utctimetuple())
                                       } for o in values] )
            return HttpResponse(json,mimetype="application/json")
        except Url.DoesNotExist:
            return Http404