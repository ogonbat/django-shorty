from shorty.piston.handler import BaseHandler
from shorty.models import Url
from shorty.utils import url_decode

class ShortenHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Url
    
    def read(self,request,url_slug=None):
        base = Url.objects
        if url_slug != None:
            return base.filter(user=request.user,id=url_decode(url_slug))
        else:
            return base.filter(user=request.user)