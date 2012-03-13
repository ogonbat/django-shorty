from piston.handler import BaseHandler
from shorty.models import Url
from shorty.utils import url_decode
from piston.utils import rc

class ShortenHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Url
    fields = ('url_field','personal_slug','status','created','private','private_password')
    
    def read(self,request,slug=None):
        base = Url.objects
        if slug != None:
            try:
                values = base.filter(user=request.user,id=url_decode(slug))
                return values
            except Url.DoesNotExist:
                return rc.NOT_HERE
        else:
            try:
                values = base.filter(user=request.user)
                return values
            except Url.DoesNotExist:
                return rc.FORBIDDEN
    
    def create(self):
        pass